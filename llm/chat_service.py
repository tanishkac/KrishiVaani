import requests
import json

class MistralChat:
    def __init__(self, host: str = "http://localhost:11434"):
        self.host = host

    def ask(self, prompt: str) -> str:
        """
        Send a single-turn prompt to the local Mistral model via Ollama API.
        """
        url = f"{self.host}/api/generate"
        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "").strip()
