# AI-Sentiment-Dashboard
Responsible AI Sentiment Dashboard for Florida Atlantic University - CAP 4630

<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/f55676d8-d356-4228-a92b-b2281a99985e" /> 

---

## Project Overview
The **AI Sentiment Dashboard** is a web-based tool that analyzes user-entered text and classifies it as **Positive**, **Negative**, or **Neutral**.

Users can type any message into the text box and click **Analyze**.  
The dashboard instantly displays:

- The **predicted sentiment** (e.g., 😊 Positive / 😐 Neutral / ☹️ Negative)  
- **Probability scores** showing model confidence  
- A brief **Responsible AI notice** reminding users that predictions are educational, probabilistic, and privacy-safe  

This project was built for **Florida Atlantic University’s CAP 4630 – Artificial Intelligence** course to demonstrate *responsible AI principles*, *machine-learning inference*, and *transparent design*.

---

## Features

### 🎯 Core Functionality
- Real-time text sentiment analysis
- Emoji-based result visualization
- Probability breakdown (e.g., Positive 70%, Neutral 20%, Negative 10%)
- FastAPI backend and interactive React frontend
- Lightweight and privacy-safe — no data storage

---

## 🤖 Responsible AI
We designed this project with **Responsible AI** principles in mind:

- **Biases:**  
  The model may reflect biases from its training data, especially around slang, cultural references, or underrepresented groups.

- **Limitations:**  
  Struggles with sarcasm, mixed emotions, or non-English text.  
  Does not provide advice, mood exercises, or next steps at this stage.

- **Data Privacy:**  
  No personal information is stored. The text is only processed to generate the sentiment label, probabilities, and emoji before being discarded.

- **Probabilities + Transparency:**  
  Probabilities show the model’s confidence (e.g., Positive: 70%, Neutral: 20%, Negative: 10%).  
  This makes the system more transparent and helps users interpret outputs responsibly.

---

## 🧰 Technical Stack
- **Frontend:** React + Vite + Axios  
- **Backend:** FastAPI (Python)  
- **Model:** Hugging Face *RoBERTa* (cardiffnlp/twitter-roberta-base-sentiment)  
- **Libraries:** PyTorch, Transformers, Uvicorn  
- **Environment:** Local / Cloud prototype  

---

## ⚙️ Installation & Usage

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload



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
