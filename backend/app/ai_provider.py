from abc import ABC, abstractmethod


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