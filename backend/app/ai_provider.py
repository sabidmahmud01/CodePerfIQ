import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class AIProvider(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass


class MockAIProvider(AIProvider):
    def generate_response(self, prompt: str) -> str:
        return (
            "Mock AI response: Based on the generated prompt, this code may have "
            "performance issues that should be reviewed. In a real version, this "
            "response would come from an LLM such as Gemini or OpenAI."
        )
    
class GeminiProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

    def generate_response(self, prompt: str) -> str:
        if not self.api_key:
            return (
                "Gemini provider is configured, but GEMINI_API_KEY is missing. "
                "Add the key to a local .env file before making real API calls."
            )

        return (
            "Gemini provider skeleton is ready. "
            "In the next version, this method will send the prompt to the Gemini API."
        )