# 💧✨ Gamma AI Watermark Remover ✨💧

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/FastAPI-brightgreen.svg?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PyMuPDF-orange.svg?style=flat-square&logo=python&logoColor=white" alt="PyMuPDF">
  <img src="https://img.shields.io/badge/Uvicorn-red.svg?style=flat-square&logo=python&logoColor=white" alt="Uvicorn">
</div>

<div align="center">
  <p> ⚠️ <b>Educational Purposes Only</b> ⚠️ </p>
</div>

---

## 🌟 What is Gamma AI Watermark Remover?

A specialized web application designed to remove **gamma.app** watermarks from PDF files. This tool specifically targets Gamma AI's branding elements that appear in PDFs exported from their free tier, helping you create clean, professional-looking documents.

## 🤔 Why do you need it?

Gamma AI is a fantastic presentation tool, but the watermarks in the free version can be problematic for professional and educational use:

* **Professional Presentations:** Remove distracting branding for business meetings and formal presentations
* **Educational Materials:** Create clean study materials and academic presentations  
* **Portfolio Work:** Present your content without third-party branding
* **Document Clarity:** Improve focus and readability by removing visual distractions

## ⚙️ How does it work?

The application uses an intelligent detection and removal system:

1. **PDF Analysis:** Parses PDF documents page by page using PyMuPDF (fitz)
2. **Targeted Detection:** Identifies gamma.app watermarks by analyzing images positioned in the bottom-right corner and links pointing to gamma.app domain
3. **Smart Removal:** Removes detected watermarks while preserving document integrity
4. **Clean Output:** Generates a watermark-free PDF ready for professional use

## 🚀 Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. **Start the Server:**
   ```bash
   python app.py
   ```

3. **Access the Web Interface:**
   Open your browser and navigate to: `http://localhost:8000`

4. **Upload and Process:**
   - Click "Choose PDF File" to select your Gamma AI PDF
   - Click "Remove Watermark" to process the file
   - Download the clean PDF automatically

---

<div align="center">
  <p>✨ <b>Enjoy your clean, professional PDFs!</b> ✨</p>
</div>
