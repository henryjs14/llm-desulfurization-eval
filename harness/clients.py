"""Send a prompt to a model and return its answer.

One function per provider, all returning the same dictionary, so the rest of the
harness does not need to know which provider it is talking to. API keys are read
from environment variables (loaded from .env by the scripts that use this module).
"""

import time

from config import MAX_ATTEMPTS, MAX_OUTPUT_TOKENS


def _ask_openai(model, prompt):
    from openai import OpenAI

    response = OpenAI().responses.create(
        model=model, input=prompt, max_output_tokens=MAX_OUTPUT_TOKENS
    )
    return {
        "text": response.output_text,
        "model_version": response.model,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }


def _ask_anthropic(model, prompt):
    import anthropic

    response = anthropic.Anthropic().messages.create(
        model=model,
        max_tokens=MAX_OUTPUT_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    return {
        "text": text,
        "model_version": response.model,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }


def _ask_google(model, prompt):
    from google import genai
    from google.genai import types

    response = genai.Client().models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(max_output_tokens=MAX_OUTPUT_TOKENS),
    )
    usage = response.usage_metadata
    return {
        "text": response.text or "",
        "model_version": response.model_version or model,
        "input_tokens": usage.prompt_token_count if usage else None,
        "output_tokens": usage.candidates_token_count if usage else None,
    }


PROVIDERS = {
    "openai": _ask_openai,
    "anthropic": _ask_anthropic,
    "google": _ask_google,
}


def ask(provider, model, prompt):
    """Send one prompt and return a dict with text, model_version, and token counts.

    Each call is independent: no conversation history and no web search, so earlier
    questions cannot influence later ones. Failed calls are retried with increasing
    waits (2, 4, 8 seconds) before the error is raised.
    """
    if provider not in PROVIDERS:
        raise ValueError(f"Unknown provider '{provider}'. Choose from {list(PROVIDERS)}.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return PROVIDERS[provider](model, prompt)
        except Exception as error:
            if attempt == MAX_ATTEMPTS:
                raise
            wait = 2 ** attempt
            print(f"    {provider} call failed ({error.__class__.__name__}); retrying in {wait}s")
            time.sleep(wait)
