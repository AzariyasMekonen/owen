import httpx
import os
import json
from typing import List, Dict, Any

class LLMClient:
    def __init__(self, api_key: str = None, model: str = "google/gemini-2.0-flash-lite-preview-02-05:free"):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY", "YOUR_OPENROUTER_API_KEY")
        self.model = model
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    async def complete(self, prompt: str, system_prompt: str = "You are a world-class software architect.") -> str:
        if self.api_key == "YOUR_OPENROUTER_API_KEY":
            # Fallback to simulated response if no key is provided
            return "Simulated LLM response: Please provide a real OpenRouter API key to enable actual architectural reasoning."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.url, headers=headers, json=data, timeout=30.0)
                response.raise_for_status()
                result = response.json()
                return result['choices'][0]['message']['content']
            except Exception as e:
                return f"Error calling LLM: {str(e)}"
