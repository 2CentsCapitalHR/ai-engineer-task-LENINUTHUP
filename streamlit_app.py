import streamlit as st
from pipeline import process_docx, generate_report_blob
import json
from io import BytesIO

st.set_page_config(page_title="Corporate Agent", layout="centered", page_icon="🤖")

st.markdown(
    """
    <style>
    .main > div { max-width: 900px; margin: 0 auto; }
    .big-title {
        font-family: "Georgia", serif;
        font-size: 36px;
        font-weight: 600;
        text-align: center;
        margin-top: 60px;
        margin-bottom: 20px;
        color: #111111;
    }
    .input-box {
        display:flex;
        justify-content:center;
        margin-bottom: 20px;
    }
    .search {
        width: 80%;
        padding: 14px 18px;
        font-size: 16px;
        border-radius: 30px;
        border: 1px solid #e6e6e6;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .subtle {
        text-align:center;
        color:#666;
        margin-bottom:30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-title">What can I help with?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle">Upload your ADGM doc or type a quick task — the agent will check it.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    uploaded = st.file_uploader("Upload a .docx file", type=["docx"], help="Upload the document to check")
    query = st.text_input("", placeholder="e.g. Validate incorporation doc / Check red flags", key="query")
    run = st.button("Run check", use_container_width=True)

st.divider()
st.header("Results")

if run:
    if (not uploaded) and (not query):
        st.warning("Please upload a .docx or enter a query to run checks.")
    else:
        st.info("Running checks — this may take a few seconds.")

        # If uploaded file exists, read bytes
        doc_bytes = None
        if uploaded:
            doc_bytes = uploaded.read()

        # Process the document (pipeline.process_docx will handle None query too)
        try:
            report = process_docx(doc_bytes, query)
        except Exception as e:
            st.error(f"Error running pipeline: {e}")
            report = {"error": str(e)}

        # Display summary
        if report.get("error"):
            st.error(report["error"])
        else:
            st.success("Processing complete.")
            st.write("**Document type:**", report.get("doc_type", "Unknown"))
            st.write("**Missing sections:**", report.get("missing_sections", []))
            st.write("**Red flags:**", report.get("red_flags", []))
            st.write("**Top ADGM citations:**")
            for c in report.get("top_citations", []):
                st.write("-", c.get("snippet", c))

            # Show Gemini suggestions if present
            gem = report.get("gemini")
            if gem:
                st.subheader("AI Suggestions")
                st.write(gem.get("text", str(gem)))

            # Download marked-up .docx and JSON report
            marked = report.get("marked_docx_bytes")
            if marked:
                st.download_button("Download marked-up .docx", data=marked, file_name="marked_up.docx")
            json_blob = json.dumps(report.get("summary", {}), indent=2)
            st.download_button("Download JSON report", data=json_blob.encode("utf-8"), file_name="report.json")
