from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import spacy

app = FastAPI()

# -------------------------------------------------------
# CORS Middleware (allow everything while developing)
# -------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------
# Load Models
# -------------------------------------------------------
# SpaCy for linguistic parsing (aspect extraction)
nlp = spacy.load("en_core_web_trf")

# Transformer model for Aspect-Based Sentiment Analysis (ABSA)
model_name = "yangheng/deberta-v3-base-absa-v1.1"
absa_tokenizer = AutoTokenizer.from_pretrained(model_name)
absa_model = AutoModelForSequenceClassification.from_pretrained(model_name)

# -------------------------------------------------------
# Request Model
# -------------------------------------------------------
class TextRequest(BaseModel):
    text: str


# -------------------------------------------------------
# Helper Function: Extract aspect-level sentences
# -------------------------------------------------------
def extract_aspect_sentences(text: str):
    doc = nlp(text)
    aspects = []
    seen = set()

    for sent in doc.sents:
        sent_candidates = []

        for chunk in sent.noun_chunks:
            ancestor = chunk.root
            verb = None
            while ancestor.head != ancestor and ancestor.head in sent:
                ancestor = ancestor.head
                if ancestor.pos_ in {"VERB", "AUX", "ADJ"}:
                    verb = ancestor
                    break

            if verb is not None:
                start_i = min(chunk.root.left_edge.i, verb.left_edge.i)
                end_i = max(chunk.root.right_edge.i, verb.right_edge.i)
            else:
                amod = None
                for child in chunk.root.children:
                    if child.dep_ == "amod":
                        amod = child
                        break
                if amod is not None:
                    start_i = chunk.root.left_edge.i
                    end_i = amod.right_edge.i
                else:
                    start_i = sent.start
                    end_i = sent.end - 1

            span_text = doc[start_i: end_i + 1].text.strip()

            if len(span_text.split()) < 2:
                continue

            if span_text not in seen:
                seen.add(span_text)
                sent_candidates.append(span_text)

        if not sent_candidates:
            s = sent.text.strip()
            if len(s.split()) >= 2 and s not in seen:
                seen.add(s)
                aspects.append(s)
        else:
            aspects.extend(sent_candidates)

    return aspects


# -------------------------------------------------------
# API Route: Analyze Sentiment
# -------------------------------------------------------
@app.post("/api/analyze")
def analyze_prompt(request: TextRequest):
    prompt = request.text.strip()
    try:
        aspects = extract_aspect_sentences(prompt)
        results = []

        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

        # Analyze each aspect individually
        for aspect in aspects:
            inputs = absa_tokenizer(aspect, return_tensors="pt", truncation=True)
            with torch.no_grad():
                outputs = absa_model(**inputs)
                probs = F.softmax(outputs.logits, dim=1)[0]
                pred_label = torch.argmax(probs).item()

            sentiment = label_map.get(pred_label, "Unknown")
            score = probs[pred_label].item()
            results.append({
                "aspect": aspect,
                "sentiment": sentiment,
                "score": round(score, 2)
            })

        # --- Compute weighted overall sentiment from aspects ---
        if results:
            weights = {"Positive": 1, "Neutral": 0, "Negative": -1}
            weighted_scores = [weights[r["sentiment"]] * r["score"] for r in results]
            avg_score = sum(weighted_scores) / len(weighted_scores)

            # interpret average sentiment
            if avg_score > 0.2:
                overall_sentiment = "Positive"
            elif avg_score < -0.2:
                overall_sentiment = "Negative"
            else:
                overall_sentiment = "Neutral"

            overall_confidence = abs(avg_score)
        else:
            # fallback: analyze full text if no aspects found
            inputs = absa_tokenizer(prompt, return_tensors="pt", truncation=True)
            with torch.no_grad():
                outputs = absa_model(**inputs)
                probs = F.softmax(outputs.logits, dim=1)[0]
                pred_label = torch.argmax(probs).item()

            overall_sentiment = label_map.get(pred_label, "Unknown")
            overall_confidence = probs[pred_label].item()

        return {
            "text": prompt,
            "overall": {
                "sentiment": overall_sentiment,
                "score": round(overall_confidence, 2)
            },
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}
