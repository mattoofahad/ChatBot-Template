"""Module doc string"""

from .config import OPENAI_API_KEY


class ConstantVariables:
    """Module doc string"""

    model_list_tuple = (
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        "o1-preview",
        "o1-mini",
    )
    provider = ("lm-studio", "OpenAI")
    default_model = "gpt-4o-mini"
    default_provider = "lm-studio"
    max_tokens = 1024
    min_token = 32
    step = 32
    default = round(((max_tokens + min_token) / 2) / step) * step
    default_token = max(min_token, min(max_tokens, default))

    if OPENAI_API_KEY != "NO_KEY":
        api_key = OPENAI_API_KEY
    else:
        api_key = ""
