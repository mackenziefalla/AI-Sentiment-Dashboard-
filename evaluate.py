# Mute the specific UserWarning about `return_all_scores` deprecation
import warnings
warnings.filterwarnings("ignore", message="`return_all_scores` is now deprecated")
# Import the HuggingFace transformers pipeline for easy access to pre-trained NLP models.
from transformers import pipeline


# Load a pre-trained sentiment analysis pipeline (RoBERTa, 3 classes: negative/neutral/positive)
sentiment_analyzer = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)


# Map model label IDs to human-readable sentiment labels.
label_map = {"LABEL_0": "🤬", "LABEL_1": "😐", "LABEL_2": "😊"}


# Repeatedly prompt the user for text, analyze sentiment, and display results.
print("\nSentiment Analysis. Press Enter on an empty line or type 'q' to quit.")
try:
    while True:
        # Get user input and strip whitespace.
        txt = input("\nEnter text: ").strip()
        # If input is empty or a quit command, exit the loop.
        if txt == "" or txt.lower() in {"q", "quit", "exit"}:
            break

        # Run the sentiment analysis model and get scores for all classes.
        all_scores = sentiment_analyzer(txt, return_all_scores=True)[0]  # list of dicts
        # Select the label with the highest score (most likely sentiment).
        top = max(all_scores, key=lambda d: d["score"])
        # Create a mapping from label to its probability score.
        probs = {d["label"]: d["score"] for d in all_scores}

        # Print the top prediction and all class probabilities.
        print(f"Prediction: {label_map[top['label']]}")
        print(
            "Probabilities: "
            f"Neg={probs.get('LABEL_0', 0):.3f}, "
            f"Neu={probs.get('LABEL_1', 0):.3f}, "
            f"Pos={probs.get('LABEL_2', 0):.3f}"
        )
except KeyboardInterrupt:
    print("\nExited.")