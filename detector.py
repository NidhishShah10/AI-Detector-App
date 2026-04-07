import requests
import os
from dotenv import load_dotenv

load_dotenv()

def detect_ai(text):
    api_key = os.getenv("SAPLING_API_KEY")

    url = "https://api.sapling.ai/api/v1/aidetect"

    payload = {
        "key": api_key,
        "text": text
    }

    # ADDED BY JUNFENG: basic request error handling
    try:
        response = requests.post(url, json=payload, timeout=30)
        result = response.json()
    except Exception as e:
        return {
            "score": None,
            "label": "Request failed",
            "status": f"error: {str(e)}"
        }
    # END ADDED BY JUNFENG

    response = requests.post(url, json=payload)
    result = response.json()

    if "msg" in result and "Rate limited" in result["msg"]:
        return {
            "score": 0,
            "label": "Rate limited - please wait and try again"
        }

    score = result.get("score", 0)
    
    if score is None:
        score = 0

    return {
        "score": round(score * 100, 2),
        "label": "AI Generated" if score > 0.5 else "Human Written"
    }

if __name__ == "__main__":
    test = "Artificial intelligence is transforming education and industry."
    print(detect_ai(test))
