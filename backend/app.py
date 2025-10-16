from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import re
import spacy

# âœ… Create the FastAPI app FIRST
app = FastAPI()

# âœ… Add CORS middleware immediately after
app.add_middleware(
    #allowing everything until app is hosted
    CORSMiddleware,
    allow_origins=["*"],  # You can later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load NLP and pipelines
nlp = spacy.load("en_core_web_sm")
absa_pipeline = pipeline("sentiment-analysis", model="yangheng/deberta-v3-base-absa-v1.1")
overall_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# ---------- Input schema ----------
class TextRequest(BaseModel):
    text: str


# ---------- Endpoint ----------
@app.post("/api/analyze")
def analyze_text(request: TextRequest):
    text = request.text.strip()

    try:
        contrast_parts = re.split(r"\b(?:but|however|though)\b", text, flags=re.IGNORECASE)
        results = []

        for part in contrast_parts:
            part = part.strip()
            if not part:
                continue

            doc = nlp(part)
            aspects = [chunk.text for chunk in doc.noun_chunks] or ["Overall"]

            absa_results = absa_pipeline(part)
            for r in absa_results:
                label = r["label"]
                score = round(r["score"] * 100, 2)
                if "#" in label:
                    asp, sentiment = label.split("#")
                else:
                    asp, sentiment = aspects[0], label
                results.append({
                    "aspect": asp.capitalize(),
                    "sentiment": sentiment.capitalize(),
                    "score": score,
                    "segment": part
                })

        overall = overall_pipeline(text)[0]
        overall_label = overall["label"]
        overall_conf = round(overall["score"] * 100, 2)

        return {
            "text": text,
            "overall": {
                "sentiment": "Positive" if overall_label == "LABEL_2" else
                             "Negative" if overall_label == "LABEL_0" else "Neutral",
                "confidence": overall_conf
            },
            "results": results
        }

    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}
