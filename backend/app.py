from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import spacy

app = FastAPI()

# Add CORS Policy MiddleWare
app.add_middleware(
    #allowing everything until app is hosted
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Larger model but more accurate - en_core_web_trf vs en_core_web_sm
nlp = spacy.load("en_core_web_trf")
model_name = "yangheng/deberta-v3-base-absa-v1.1"
absa_tokenizer = AutoTokenizer.from_pretrained(model_name)
absa_model = AutoModelForSequenceClassification.from_pretrained(model_name)

class TextRequest(BaseModel):
    text: str

    
def extract_aspect_sentences(text: str):
    #Split prompt into aspects using spacy
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

            span_text = doc[start_i : end_i + 1].text.strip()

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

@app.post("/api/analyze")
def analyze_prompt(request: TextRequest):
    prompt = request.text.strip()
    try:
        aspects = extract_aspect_sentences(prompt)
        results = []

        #Analyze each aspect and append its result to results
        for aspect in aspects:
            inputs = absa_tokenizer(aspect, return_tensors="pt", truncation=True)
            with torch.no_grad():
                outputs = absa_model(**inputs)
                probs = F.softmax(outputs.logits, dim=1)[0]
                pred_label = torch.argmax(probs).item()

            label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
            sentiment = label_map.get(pred_label, "Unknown")
            results.append({"aspect": aspect, "sentiment": sentiment, "score": "%.2f" % probs[pred_label].item()})

        #Analyse entire sentence using ASBA model and append it as overall aspect
        inputs = absa_tokenizer(prompt, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = absa_model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)[0]
            pred_label = torch.argmax(probs).item()

        overall_sentiment_pred = label_map.get(pred_label, "Unknown")
        confidence = probs[pred_label].item()

        return {
            "text": prompt,
            "overall": {
                "sentiment": overall_sentiment_pred,
                "score": "%.2f" % confidence,
            },
            "results": results
        }
    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}