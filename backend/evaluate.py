# Suppress return_all_scores warning
import warnings
warnings.filterwarnings("ignore", message="`return_all_scores` is now deprecated")

from transformers import pipeline
import nltk

# Download punkt tokenizer if not already present
nltk.download("punkt", quiet=True)
from nltk.tokenize import sent_tokenize

# Load pre-trained sentiment model (fast + contextual)
sentiment_analyzer = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

# Map model labels to readable names
label_map = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}

def analyze_prompt(prompt: str):
    """
    Analyze a full prompt and detect per-sentence sentiment ("aspect-style").
    """
    sentences = sent_tokenize(prompt)
    results = []

    for sent in sentences:
        scores = sentiment_analyzer(sent, return_all_scores=True)[0]
        top = max(scores, key=lambda d: d["score"])
        probs = {label_map[d["label"]]: round(d["score"], 3) for d in scores}
        results.append({
            "aspect": sent.strip(),
            "sentiment": label_map[top["label"]],
            "probabilities": probs
        })

    # If multiple sentiments exist, summarize overall sentiment
    sentiments = [r["sentiment"] for r in results]
    overall = max(set(sentiments), key=sentiments.count)

    return {
        "overall_sentiment": overall,
        "aspects": results
    }
# # Mute the specific UserWarning about `return_all_scores` deprecation
# from tokenize import String
# import warnings
# warnings.filterwarnings("ignore", message="`return_all_scores` is now deprecated")
# # Import the HuggingFace transformers pipeline for easy access to pre-trained NLP models.
# from transformers import pipeline


# # Load a pre-trained sentiment analysis pipeline (RoBERTa, 3 classes: negative/neutral/positive)
# sentiment_analyzer = pipeline(
#     task="sentiment-analysis",
#     model="cardiffnlp/twitter-roberta-base-sentiment"
# )


# # Map model label IDs to human-readable sentiment labels.
# label_map = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}


# def test_model():
#     print("\nSentiment Analysis. Press Enter on an empty line or type 'q' to quit.")
#     try:
#         while True:
#             # Get user input and strip whitespace.
#             txt = input("\nEnter text: ").strip()
#             # If input is empty or a quit command, exit the loop.
#             if txt == "" or txt.lower() in {"q", "quit", "exit"}:
#                 break

#             # Run the sentiment analysis model and get scores for all classes.
#             all_scores = sentiment_analyzer(txt, return_all_scores=True)[0]  # list of dicts
#             # Select the label with the highest score (most likely sentiment).
#             top = max(all_scores, key=lambda d: d["score"])
#             # Create a mapping from label to its probability score.
#             probs = {d["label"]: d["score"] for d in all_scores}

#             # Print the top prediction and all class probabilities.
#             print(f"Prediction: {label_map[top['label']]}")
#             print(
#                 "Probabilities: "
#                 f"Neg={probs.get('LABEL_0', 0):.3f}, "
#                 f"Neu={probs.get('LABEL_1', 0):.3f}, "
#                 f"Pos={probs.get('LABEL_2', 0):.3f}"
#             )
#     except KeyboardInterrupt:
#         print("\nExited.")

# def analyze_prompt(prompt: str):
#     all_scores = sentiment_analyzer(prompt, return_all_scores=True)[0]
#     top = max(all_scores, key=lambda d: d["score"])
#     return label_map[top['label']]
