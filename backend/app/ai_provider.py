import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from google import genai

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

        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def generate_response(self, prompt: str) -> str:
        if not self.api_key or not self.client:
            return (
                "Gemini provider is configured, but GEMINI_API_KEY is missing. "
                "Add the key to backend/.env before making real API calls."
            )

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as error:
            return f"Gemini API error: {str(error)}"
        
def get_ai_provider() -> AIProvider:
    provider_name = os.getenv("AI_PROVIDER", "mock").lower()

    if provider_name == "gemini":
        return GeminiProvider()

    return MockAIProvider()