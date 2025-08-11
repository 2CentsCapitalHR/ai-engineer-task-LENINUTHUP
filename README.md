# Corporate Agent Prototype (Streamlit)

This prototype demonstrates an end-to-end minimal pipeline for an ADGM-compliant corporate agent.

## What's included
- `streamlit_app.py` - Streamlit UI (upload .docx, run checks, download marked-up docx + json report)
- `pipeline.py` - Backend processing scaffold (parsing, simple classification, checklist, red-flag detection, docx markup)
- `/samples` - sample .docx files (incorporation_resolution.docx, employment_contract.docx, malformed_document.docx)
- `requirements.txt` - suggested Python packages
- `run_demo.sh` - quick launcher script
- Extracted ADGM references (if PDF parsing was successful): `data/adgm_references.txt`

## How to run (local)
1. Install Python 3.10+
2. (Optional) Create a venv:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\Scripts\activate     # Windows (PowerShell)
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your Gemini API key (if you will run RAG/LLM features):
   ```bash
   export GEMINI_API_KEY="your_key_here"    # macOS / Linux
   setx GEMINI_API_KEY "your_key_here"      # Windows (restart shell)
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Notes
- The repo includes a scaffold for Gemini RAG integration; actual Gemini calls are not included and will be wired after you add your API key.
- The pipeline is intentionally simple so you can extend it quickly for your interview test.
