"""Print the model IDs available to your API keys, to check the names in config.py.

Usage (from the repository root):
    python harness/list_models.py
"""

import os

from dotenv import load_dotenv


def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY"):
        from openai import OpenAI
        print("OpenAI:")
        for m in sorted(m.id for m in OpenAI().models.list()):
            print("  ", m)

    if os.getenv("ANTHROPIC_API_KEY"):
        import anthropic
        print("Anthropic:")
        for m in anthropic.Anthropic().models.list():
            print("  ", m.id)

    if os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
        from google import genai
        print("Google:")
        for m in genai.Client().models.list():
            if "generateContent" in (m.supported_actions or []):
                print("  ", m.name.removeprefix("models/"))


if __name__ == "__main__":
    main()
