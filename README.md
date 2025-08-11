# Corporate Agent Prototype (Streamlit)

This project is a **proof-of-concept corporate document review assistant** built using [Streamlit](https://streamlit.io/).  
It demonstrates an **end-to-end minimal pipeline** for an **ADGM-compliant corporate agent** — capable of parsing corporate documents, running basic compliance checks, identifying potential red flags, and producing both a marked-up `.docx` file and a JSON compliance report.

---

##  What's Included

### **Source Code & Scripts**
- **`streamlit_app.py`**  
  Main Streamlit UI.  
  - Upload `.docx` files.  
  - Run backend processing.  
  - Download marked-up document + JSON compliance report.
  
- **`pipeline.py`**  
  Backend processing scaffold:  
  - Parses `.docx` files.  
  - Performs basic classification.  
  - Runs compliance checklist.  
  - Detects red flags.  
  - Adds inline `.docx` comments.

- **`requirements.txt`** — Python dependencies.
- **`run_demo.sh`** — Quick demo launcher.

### **Sample Data**
- `/samples`:
  - `incorporation_resolution.docx`
  - `employment_contract.docx`
  - `malformed_document.docx`

### **Reference Data**
- `data/adgm_references.txt` — Extracted ADGM references (if PDF parsing was successful).

---

##  Local Installation & Running

### 1. Install Python
Ensure **Python 3.10+** is installed:
```bash
python --version
```

### 2. (Optional) Create & Activate a Virtual Environment
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Gemini API Key *(Optional, for RAG/LLM features)*
```bash
# macOS / Linux
export GEMINI_API_KEY="your_key_here"

# Windows (PowerShell)
setx GEMINI_API_KEY "your_key_here"
# Restart terminal after setting
```
*Without the API key, only basic parsing and red-flag checks will run.*

### 5. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```
Access the app at: [http://localhost:8501](http://localhost:8501)

---

##  Usage Guide

1. **Upload a Document** (`.docx` format only).  
2. **Run Checks** — Backend will:
   - Parse the document.
   - Identify type (classification).
   - Compare content against compliance checklist.
   - Detect red flags.
   - Add inline comments to `.docx`.
3. **Download Results**:
   - Marked-up `.docx` with comments.
   - JSON report with findings.

---

##  Output
<img width="630" height="399" alt="Screenshot 2025-08-11 181034" src="https://github.com/user-attachments/assets/737d8092-c1a3-40cd-8b00-1e3154200f6f" />

<img width="767" height="484" alt="Screenshot 2025-08-11 181109" src="https://github.com/user-attachments/assets/7bc7374e-5080-40fc-ae61-3ec3e198ea5d" />

<img width="725" height="580" alt="Screenshot 2025-08-11 181136" src="https://github.com/user-attachments/assets/6f568879-5014-4e9b-ad07-5673ff37b801" />

<img width="782" height="372" alt="Screenshot 2025-08-11 181150" src="https://github.com/user-attachments/assets/a7e4786c-2b75-43f5-8dd7-7db7e6b4b45a" />

##  Notes
- Pipeline is **intentionally minimal** to allow quick customization.
- **Gemini RAG integration** scaffold included but inactive until you configure your API key.
- Designed for **proof-of-concept** and **interview test** use.

---

##  Future Integrations

Planned enhancements include:
- **Full Gemini RAG Integration**  
  - Document chunking and semantic search.  
  - Context-aware LLM responses.
- **Support for Additional File Formats** (`.pdf`, `.txt`).
- **Multi-Language Document Analysis** (Arabic, Hindi, etc.).
- **Advanced NLP Features**:
  - Named Entity Recognition (NER).  
  - Contract clause extraction.
- **Customizable Compliance Checklists** per jurisdiction.
- **Integration with Document Management Systems (DMS)** for automated ingestion.
- **Dashboard & Analytics View**:
  - Track common compliance issues.  
  - Monitor review statistics over time.
- **User Role Management** for multi-user corporate environments.
- **Automated Red-Flag Severity Scoring** for prioritization.

---

##  License
This project is provided as-is for educational and demonstration purposes.
