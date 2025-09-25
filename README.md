# AI-Sentiment-Dashboard
Responsible AI Sentiment Dashboard for class CAP 4630



<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/f55676d8-d356-4228-a92b-b2281a99985e" /> 

## Project Overview
The AI Sentiment Dashboard is a web application that analyzes text and classifies it as positive, negative, or neutral. Users can input text, and the system will return both a sentiment label and probability scores to show how confident the model is. An emoji is also displayed alongside the result for easy interpretation.
This project was developed as part of a class assignment at Florida Atlantic University to explore Responsible AI, machine learning deployment, and transparent design practices.

## Features


## Responsible AI 
We designed this project with responsible AI principles in mind:

-Biases :
The model may reflect biases from its training data, especially around slang, cultural references, or underrepresented groups.

-Limitations :
Struggles with sarcasm, mixed emotions, or non-English text.
Does not provide advice, mood exercises, or next steps at this stage.

-Data Privacy :
No personal information is stored. The text is only processed to generate the sentiment label, probabilities, and emoji before being discarded.

-Probabilities + Explanations for Transparency :
Probabilities show the model’s confidence (e.g., Positive: 70%, Neutral: 20%, Negative: 10%).
Explanations highlight which words/phrases influenced the result.
This makes the system more transparent and helps users interpret outputs responsibly.

## Technical Stack
-Model: Hugging Face RoBERTa

## Installation & Usage


## Future Improvements
-Multilanguage support.
-Improve handling sarcasm and mixed emotions.

## Contributors 

-Machine Learning Lead – Christopher Piedra

-Backend Developer – Matthew White

-Frontend Developer – Matthew Wyatt

-Data Engineer – Sophia Camacho

-Responsible AI & Documentation Lead / PM – Mackenzie Falla

# ALL PREDICTIONS ARE PROBABILISTIC AND NOT DETERMINISTIC
