# 💧✨ Gamma AI Watermark Remover (v2.0 Refactored) ✨💧

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

## 🌟 Gamma PDF Watermark Remover: Refactored Edition

This is a significantly improved and refactored version of the original [gamma-ai-watermark-remover](https://github.com/DedInc/gamma-ai-watermark-remover) project. This edition has been completely re-engineered for enhanced efficiency, maintainability, and security, with major contributions from **[Daniel Guerrero](https://github.com/danielxxomg)**.

This tool is designed for anyone who needs to present documents without the distraction of third-party branding, making it ideal for students, educators, and professionals.

## 🤔 Why This Version?

While the original tool was functional, this version introduces critical improvements:

*   **Optimized Architecture:** The PDF processing logic has been consolidated into a single, efficient module (`pdf_processor.py`), adhering to the Single Responsibility Principle.
*   **Improved Performance:** The workflow now operates on a single-pass read/write basis, reducing I/O overhead and increasing speed.
*   **Reduced Dependencies:** The `Werkzeug` dependency has been eliminated by implementing an internal `secure_filename` function, making the project more lightweight.
*   **Clean & Maintainable Code:** `app.py` has been refactored for clarity, and obsolete files have been removed, resulting in a cleaner, more maintainable codebase.

## ⚙️ How It Works

The detection and removal system has been optimized for precision and performance:

1.  **Efficient PDF Parsing:** It uses `PyMuPDF` to analyze the document in a single, efficient operation.
2.  **Accurate Detection:** It identifies `gamma.app` watermarks by analyzing images in the bottom-right corner and their associated hyperlinks.
3.  **Single-Pass Removal:** It removes the detected elements and saves the new PDF in a single, streamlined workflow.
4.  **Clean Output:** The result is a clean, watermark-free PDF, ready for professional use.

## 🚀 Getting Started

Follow these steps to set up your development environment.

### 1. Clone the Repository

```bash
git clone https://github.com/danielxxomg/gamma-pdf-watermark-remover.git
cd gamma-pdf-watermark-remover
```

### 2. Create and Activate a Virtual Environment

Using a virtual environment is a best practice for managing project dependencies.

**Create the environment:**
```bash
python -m venv venv
```

**Activate the environment:**
- On **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- On **macOS & Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt --upgrade
```

### 4. Run the Server

```bash
python app.py
```

### 5. Access the Web Interface
Open your browser and navigate to: `http://localhost:8000`

### 6. Upload and Process
- Click "Choose PDF File" to select your Gamma AI PDF.
- Click "Remove Watermark" to process the file.
- The cleaned PDF will be downloaded automatically.

---

## 🙏 Acknowledgements

*   **Original Author:** [Vladislav Zenkevich (DedInc)](https://github.com/DedInc) for creating the initial proof-of-concept.
*   **Lead Contributor (Refactoring):** [Daniel Guerrero](https://github.com/danielxxomg) for the complete re-engineering, optimization, and security enhancements.

<div align="center">
  <p>✨ <b>Enjoy your clean, professional PDFs!</b> ✨</p>
</div>
