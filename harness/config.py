"""Settings for the evaluation harness.

Edit this file to change which models are tested or which model grades the answers.
Model IDs change as providers release new versions; run `python harness/list_models.py`
to see the IDs currently available to your API keys.
"""

# Models under test, keyed by provider. Each must have an API key in .env.
MODELS = {
    "openai": "gpt-6.1-sol",
    "google": "gemini-4-argon",
    "anthropic": "claude-opus-5-5",
}

# Model used to grade answers against the rubrics.
# Note: a grader may favor answers from its own provider. Grades are validated
# against expert grading of a sample before results are reported.
GRADER = ("anthropic", "claude-opus-5-5")

# Upper limit on the length of each model response, in tokens.
MAX_OUTPUT_TOKENS = 4000

# Number of attempts per API call before giving up (covers rate limits and
# temporary server errors).
MAX_ATTEMPTS = 4

# File locations, relative to the repository root.
QUESTION_BANK = "question_bank.md"
RESULTS_DIR = "results"
