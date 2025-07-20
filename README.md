# 🤖 AI Resume Matcher using Mistral 7B (Local LLM - No Internet Required)

This project is a Python-based intelligent resume screening tool powered by Mistral 7B Instruct (Q5_K_M GGUF) running locally on your CPU/GPU.  
It matches multiple resumes against a single job description, scores them with a match percentage, provides detailed reasoning, and saves the result in Word documents automatically.

---

[▶️ Watch Demo on YouTube](https://youtu.be/5H88hSNtpvM)

---

## 🚀 Features

- Takes unlimited resumes from the `data/resumes` folder  
- Uses a powerful LLM (Mistral 7B Instruct) locally via ctransformers  
- Analyzes each resume with your job description  
- Outputs a detailed Word file for each candidate (saved in `results/`)  
- Runs fully offline after setup (no API keys or cloud costs)

---

## 📂 Project Structure

AI-Resume-Matcher/  
├── app.py                   - Main script  
├── reasoner.py              - Handles LLM-based reasoning  
├── utils.py                 - Resume text extraction  
├── models/                  - Place Mistral model file here  
│   └── mistral-7b-instruct-v0.1.Q5_K_M.gguf  
├── data/  
│   └── resumes/             - Add candidate PDF resumes here  
├── results/                 - Output Word files stored here  
├── download_model.bat      - One-click model downloader for Windows  
├── requirements.txt  
├── LICENSE  
└── README.md

---

## 🧠 Model Setup (Required)

GitHub doesn’t allow files larger than 100MB, so you must manually download the LLM model or use the BAT script provided.

### Option 1: Manual Download

1. Go to this Hugging Face page:  
   https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

2. Download the file:  
   mistral-7b-instruct-v0.1.Q5_K_M.gguf

3. Place it into the `models` folder like this:  
   models/mistral-7b-instruct-v0.1.Q5_K_M.gguf

### Option 2: Use BAT Script (Windows Only)
Instead of downloading manually, run the file:  
download_model.bat

It will automatically:
- Create the `models` folder (if not present)
- Download the correct .gguf model file

---

## 📥 How to Use

Step 1: Install Requirements  
pip install -r requirements.txt

Step 2: Add Resumes  
Place any number of .pdf resume files inside:  
data/resumes/

Step 3: Run the App  
python app.py

You will be prompted to enter:
- The job title  
- The job description (paste full text)

Then the script will:
- Parse all resumes  
- Match them with the job  
- Save a detailed .docx file for each in the results folder

---

## 📄 Output Example

For each resume, a Word document will be generated with:
- Job title and description  
- Resume filename  
- Match percentage (0–100%)  
- Reasoning explaining:  
  - Skills that match  
  - Missing qualifications  
  - Strengths and red flags

---

## 📄 Requirements
- Python 3.9–3.11  
- RAM: At least 8–16GB  
- Works on: Windows, Mac, Linux  
- GPU recommended (but not required)

---

## 🪪 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Made by [Aarav Mehta](https://github.com/AaravMehta-07)

---

## ⭐ Star the repo if you find it helpful!
