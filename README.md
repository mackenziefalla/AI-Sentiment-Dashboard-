# 🧠 AI-Sentiment-Dashboard
**Responsible AI Sentiment Dashboard for Florida Atlantic University **

Link for Powerpoint: https://1drv.ms/p/c/6c383511022771d7/EW9zlOjly_RIvPyB5oOc7LgB9Kawy8fz8QU_1W5IMGtXVQ

---

<img width="500" height="250" alt="AI Sentiment Dashboard Screenshot" src="https://github.com/user-attachments/assets/f55676d8-d356-4228-a92b-b2281a99985e" />

---

##  Project Overview
The **AI Sentiment Dashboard** is a web-based tool that analyzes user-entered text and classifies it as **Positive**, **Negative**, or **Neutral**.

Users can type any message into the text box and click **Analyze**.  
The dashboard instantly displays:

- The **predicted sentiment** (e.g., 😊 Positive / 😐 Neutral / ☹️ Negative)  
- **Probability scores** showing model confidence  
- A short **Responsible AI notice** reminding users that predictions are educational, probabilistic, and privacy-safe  

This project was built for **Florida Atlantic University’s CAP 4630 – Artificial Intelligence** course to demonstrate responsible AI principles, model deployment, and transparent design.

---

##  Features

###  Core Functionality
- Real-time text sentiment analysis  
- Emoji-based result visualization  
- Probability breakdown (e.g., Positive 70%, Neutral 20%, Negative 10%)  
- **FastAPI backend** + **React frontend** integration  
- Lightweight and privacy-safe — no data storage  

---

##  Responsible AI
This project follows **Responsible AI** principles to ensure transparency and fairness.

### **Biases**
The model may reflect biases from its training data, especially around slang, cultural references, or underrepresented groups.

### **Limitations**
- Struggles with sarcasm, mixed emotions, or non-English text  
- Does not provide advice, emotional guidance, or next steps  

### **Data Privacy**
No personal information is stored.  
User text is processed once to generate results and then discarded immediately.

### **Probabilities & Transparency**
The system shows model confidence, e.g.  
**Positive: 70% | Neutral: 20% | Negative: 10%**  
This helps users interpret outputs responsibly and understand uncertainty.

---

## Technical Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | React + Vite + Axios |
| **Backend** | FastAPI (Python) |
| **Model** | Hugging Face RoBERTa (`cardiffnlp/twitter-roberta-base-sentiment`) |
| **Libraries** | PyTorch, Transformers, Uvicorn |
| **Environment** | Local development / Cloud prototype |

---

## Installation & Usage

## System Architecture

The AI Sentiment Dashboard follows a simple and transparent architecture consisting of three core layers:

1. **Frontend (React)**  
   - Handles user input through a web interface.  
   - Sends the text to the backend using Axios.  
   - Displays the sentiment label, emoji, and confidence scores returned from the backend.  

2. **Backend (FastAPI – Python)**  
   - Acts as an intermediary between the frontend and the machine learning model.  
   - Exposes a REST API endpoint (`/analyze`) to receive text input.  
   - Passes user text to the sentiment analysis model and returns the results.  

3. **Model Layer (Hugging Face RoBERTa)**  
   - Processes the text using a pre-trained transformer model.  
   - Generates probability scores for **Positive**, **Negative**, and **Neutral** sentiment.  
   - Sends the final results back to the backend in JSON format.  

4. **Results Display (Frontend Output)**  
   - The frontend updates the UI with:  
     - The predicted sentiment (😊 / 😐 / ☹️)  
     - Probability scores (e.g., Positive 72%, Neutral 18%, Negative 10%)  
     - A brief Responsible AI notice about data privacy and interpretability.
## All requirements:
- A list of all requirements: 
annotated-doc==0.0.3
annotated-types==0.7.0
anyio==4.11.0
blis==1.3.0
catalogue==2.0.10
certifi==2025.10.5
charset-normalizer==3.4.4
click==8.3.0
cloudpathlib==0.23.0
colorama==0.4.6
confection==0.1.5
curated-tokenizers==0.0.9
curated-transformers==0.1.1
cymem==2.0.11
en_core_web_trf @ https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.8.0/en_core_web_trf-3.8.0-py3-none-any.whl
fastapi==0.121.0
filelock==3.20.0
fsspec==2025.10.0
huggingface-hub==0.36.0
idna==3.11
Jinja2==3.1.6
MarkupSafe==3.0.3
mpmath==1.3.0
murmurhash==1.0.13
networkx==3.5
numpy==2.3.4
packaging==25.0
preshed==3.0.10
protobuf==6.33.0
pydantic==2.12.4
pydantic_core==2.41.5
PyYAML==6.0.3
regex==2025.11.3
requests==2.32.5
safetensors==0.6.2
sentencepiece==0.2.1
smart_open==7.4.4
sniffio==1.3.1
spacy==3.8.8
spacy-curated-transformers==0.3.1
spacy-legacy==3.0.12
spacy-loggers==1.0.5
srsly==2.5.1
starlette==0.49.3
sympy==1.14.0
thinc==8.3.8
tiktoken==0.12.0
tokenizers==0.22.1
torch==2.9.0
tqdm==4.67.1
transformers==4.57.1
typer-slim==0.20.0
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.5.0
wasabi==1.1.3
weasel==0.4.2
wrapt==2.0.1

## Flow Summary 
1. User enters text on the dashboard
2. Frontend sends the request to the FastAPI backend
3. Backend runs inference with RoBERTa
4. Model returns sentiment + probabilities
5. Frontend displays the result with an emoji

## Future Improvements 
- Multi-language support
- Improved handling of sarcasm and mixed emotions
- Add word-level explainability visualization
- Deploy to AWS for public access

## Contributors 
- **Machine Learning Lead –** Christopher Piedra  
- **Backend Developer –** Matthew White  
- **Frontend Developer –** Matthew Wyatt  
- **Data Engineer –** Sophia Camacho  
- **Responsible AI & Documentation Lead / PM –** Mackenzie Falla



---

# ⚠️ ALL PREDICTIONS ARE PROBABILISTIC AND NOT DETERMINISTIC
> No personal data is stored.  
> Predictions are generated locally and are for educational use only under **FAU’s CAP 4630 – Artificial Intelligence**.


