# 🛡️ Cyberbullying Detection System using Agentic AI Architecture with Gemini LLM

An intelligent cyberbullying detection system that combines Google's Gemini Large Language Model (LLM) with a modular Agentic AI architecture to classify bullying messages, assess risk levels, and generate supportive responses. The project also evaluates the effectiveness of LLM prompting techniques (Zero-Shot and Few-Shot Prompting) against a traditional Rule-Based System.

**Tech Stack:** Python · Streamlit · Google Gemini 3.1 Flash Lite · Google Generative AI API · Scikit-learn · Pandas

---

# Problem Statement

Cyberbullying has become a growing concern, particularly among teenagers and young adults who actively communicate through digital platforms. Existing keyword-based detection systems often fail to understand the semantic meaning and context of messages, resulting in inaccurate classifications and high false positive rates.

Although Large Language Models (LLMs) have demonstrated strong natural language understanding capabilities, many existing systems only perform simple text classification without providing additional analysis or user support.

This project addresses these limitations by implementing an Agentic AI-inspired architecture that separates the analysis into multiple reasoning modules while comparing its performance against a traditional Rule-Based approach.

---

# Project Objectives

- Develop an intelligent cyberbullying detection system using Gemini LLM.
- Implement a modular Agentic AI architecture consisting of message classification, risk assessment, and supportive response generation.
- Compare the proposed LLM-based approach against a Rule-Based baseline.
- Evaluate the impact of Zero-Shot Prompting and Few-Shot Prompting on classification performance.

---

# System Overview

The proposed system performs cyberbullying analysis through several sequential modules instead of relying on a single prediction.

```
                User Message
                     │
                     ▼
          Text Pre-processing Module
                     │
                     ▼
      ┌────────────────────────────────┐
      │ Classification Module          │
      │ Gemini 3.1 Flash Lite          │
      └────────────────────────────────┘
                     │
                     ▼
      ┌────────────────────────────────┐
      │ Risk Assessment Module         │
      │ Gemini 3.1 Flash Lite          │
      └────────────────────────────────┘
                     │
                     ▼
      ┌────────────────────────────────┐
      │ Support Response Module        │
      │ Gemini 3.1 Flash Lite          │
      └────────────────────────────────┘
                     │
                     ▼
             Final System Output
```

Unlike a chatbot framework, this project manually implements the Agentic AI workflow using Python while adopting the modular reasoning concept inspired by CrewAI architecture.

---

# Architecture

The system consists of five main components:

- **User Interface**
  - Built using Streamlit.
  - Accepts user input and displays analysis results.

- **Text Pre-processing**
  - Text cleaning
  - Lowercase conversion
  - URL removal
  - Mention removal
  - Hashtag removal
  - Special character removal

- **Classification Module**
  - Determines whether the message contains cyberbullying.
  - Predicts bullying category:
    - Gender
    - Religion
    - Age
    - Ethnicity
    - Other Cyberbullying
    - Not Cyberbullying

- **Risk Assessment Module**
  - Determines the severity of the detected bullying.
  - Predicts:
    - Low
    - Medium
    - High

- **Support Response Module**
  - Generates an empathetic response to guide users appropriately.

---

# Dataset

Dataset used:

**Cyberbullying Tweets Dataset (Kaggle)**

Contains approximately **47,000** labelled tweets covering multiple cyberbullying categories.

Labels include:

- not_cyberbullying
- gender
- religion
- age
- ethnicity
- other_cyberbullying

---

# Evaluation Methodology

The proposed system was evaluated using three different approaches.

## 1. Rule-Based System

A traditional baseline system using manually defined keyword matching rules.

Characteristics:

- Keyword matching
- Fast execution
- No contextual understanding

---

## 2. Gemini LLM using Zero-Shot Prompting

The model receives only task instructions without examples.

Prompt includes:

- Bullying detection
- Category prediction
- Severity prediction

---

## 3. Gemini LLM using Few-Shot Prompting

The model receives several labelled examples before classifying new messages.

This provides better guidance for category prediction and improves classification consistency.

---

# Experimental Results

| Method | Accuracy | Weighted F1-Score |
|---------|----------|-------------------|
| Rule-Based System | 48.5% | 0.53 |
| Gemini Zero-Shot | 61.3% | 0.66 |
| Gemini Few-Shot | **67.5%** | **0.72** |

The experimental results demonstrate that the proposed Gemini-based approach consistently outperformed the Rule-Based baseline.

Few-Shot Prompting achieved the highest overall accuracy and F1-score by providing the model with labelled examples before prediction, allowing better semantic understanding of cyberbullying messages.

---

# Key Features

- Cyberbullying Detection
- Bullying Category Classification
- Risk Level Assessment
- Supportive Response Generation
- Streamlit Web Interface
- Agentic AI-inspired Modular Architecture
- Rule-Based Baseline Comparison
- Zero-Shot Prompting
- Few-Shot Prompting
- Performance Evaluation using Scikit-learn

---

# Setup & Installation

## Prerequisites

- Python 3.10+
- Google Gemini API Key

---

## 1. Clone Repository

```bash
git clone https://github.com/yuven15nach/cyberbullying-detection-system.git

cd cyberbullying-detection-system
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create Environment File

Create a file named

```
.env
```

Add your Gemini API Key

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# Running System Evaluation

The evaluation scripts are located inside the `evaluation/` folder.

Run:

```bash
python -m evaluation.test_model
```

The script automatically:

- Reads the evaluation dataset
- Performs text preprocessing
- Sends each message to Gemini
- Parses predictions
- Normalizes labels
- Calculates evaluation metrics
- Generates classification report
- Produces confusion matrix

---

# Project Structure

```
cyberbullying-detection-system/

│
├── app.py                         # Streamlit application
├── requirements.txt
├── README.md
├── .gitignore
│
├── crew/
│   └── crew_setup.py              # Agentic analysis pipeline
│
├── utils/
│   ├── gemini_api.py
│   └── preprocessing.py
│
├── detectors/
│   └── rule_based.py              # Rule-Based baseline
│
├── evaluation/
│   ├── evaluate_classifier.py
│   ├── metrics.py
│   ├── parse_output.py
│   └── test_model.py
│
├── data/
│   └── cyberbullying_tweets.csv
```

---

# Technologies Used

- Python
- Streamlit
- Google Gemini 3.1 Flash Lite
- Google Generative AI API
- Pandas
- Scikit-learn
- Matplotlib
- Python-dotenv

---

# Future Improvements

- Fine-tune an open-source LLM specifically for cyberbullying detection.
- Incorporate multilingual cyberbullying datasets.
- Add conversation history for contextual analysis.
- Deploy using cloud infrastructure for real-time public access.
- Introduce explainable AI techniques for improved decision transparency.

---

# Research Contribution

Unlike traditional cyberbullying detection systems that rely solely on keyword matching, this project demonstrates how a modular Agentic AI-inspired architecture combined with Gemini LLM can improve cyberbullying detection while simultaneously providing contextual risk assessment and supportive responses.

The comparison between Rule-Based, Zero-Shot Prompting, and Few-Shot Prompting further highlights the effectiveness of prompt engineering in improving LLM classification performance.

---

# Author

**Yuven Nach**

Bachelor of Computer Science (AI) with Honours

UNIVERSITI KEBANGSAAN MALAYSIA (UKM)
NATIONAL UNIVERSITY OF MALAYSIA 

Final Year Project (FYP)