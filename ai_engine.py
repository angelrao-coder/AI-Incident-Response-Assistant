
import urllib.request
import json


def generate_ai_report(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }

    try:

        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            }
        )

        with urllib.request.urlopen(
            request, timeout=180
        ) as response:

            result = json.loads(
                response.read().decode("utf-8")
            )

        return result["response"]

    except Exception as error:

        return (
            "AI connection failed.\n"
            "Make sure Ollama is running and "
            "the model is downloaded.\n"
            f"Error: {error}"
        )

