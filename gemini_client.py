
import os, time

try:
    import google.generativeai as genai
except ImportError:
    genai = None

API_KEY = os.getenv("GEMINI_API_KEY")

def _mock_response(prompt, context=None):
    summary = "Mocked Gemini response: This document appears to be an incorporation-style document. Recommended: verify Memorandum of Association, clarify beneficiary clauses, and remove 'sole discretion' phrasing."
    suggestions = [
        "Add a clear beneficiary disclosure section.",
        "Replace 'sole discretion' with defined approval process.",
        "Add registered address and shareholder agreement references."
    ]
    return {"text": summary, "suggestions": suggestions, "timestamp": time.time()}

def generate_completion(prompt: str, context: str = None, model: str = "gemini-1.5-flash"):
    """
    Generate a completion using Google's Gemini model.
    If API key or SDK not available, returns mock response.
    """
    if not API_KEY or genai is None:
        return _mock_response(prompt, context)

    try:
        genai.configure(api_key=API_KEY)
        full_prompt = prompt
        if context:
            full_prompt += "\n\nContext:\n" + context

        model_obj = genai.GenerativeModel(model)
        response = model_obj.generate_content(full_prompt)

        if hasattr(response, "text"):
            return {"text": response.text, "raw": response}
        else:
            return {"text": str(response), "raw": response}
    except Exception as e:
        raise  # so we see the real error in the terminal

if __name__ == "__main__":
    print("gemini_client self-test")
    print(generate_completion("Test prompt for Gemini API"))
