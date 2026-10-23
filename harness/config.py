"""Settings for the evaluation harness.

Edit this file to change which models are tested or which model grades the answers.
Model IDs change as providers release new versions; run `python harness/list_models.py`
to see the IDs currently available to your API keys.
"""

# Models under test: (label, provider, model ID). The label names the model in
# results tables. Each provider used needs an API key in .env.
MODELS = [
    ("gpt-6-astra", "openai", "gpt-6-astra"),
    ("gpt-6.1-sol", "openai", "gpt-6.1-sol"),
    ("gpt-6-luna", "openai", "gpt-6-luna"),
    ("gemini-4-argon", "google", "gemini-4-argon"),
    ("claude-fable-5-1", "anthropic", "claude-fable-5-1"),
]

# Model used to grade answers against the rubrics.
# Note: a grader may favor answers from its own provider. Grades are validated
# against expert grading of a sample before results are reported.
GRADER = ("anthropic", "claude-opus-5-5")

# Upper limit on the length of each model response, in tokens. For reasoning
# models this includes internal reasoning; answers that hit the limit are
# flagged as truncated in the results.
MAX_OUTPUT_TOKENS = 4000

# Number of attempts per API call before giving up (covers rate limits and
# temporary server errors).
MAX_ATTEMPTS = 4

# File locations, relative to the repository root.
QUESTION_BANK = "question_bank.md"
RESULTS_DIR = "results"
