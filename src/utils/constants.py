"""Module doc string"""

from .config import OPENAI_API_KEY


class ConstantVariables:
    """Module doc string"""

    model_list_tuple = (
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-4",
        "gpt-3.5-turbo",
    )
    default_model = "gpt-4o-mini"

    max_tokens = 180
    min_token = 20
    step = 20
    default = round(((max_tokens + min_token) / 2) / step) * step
    default_token = max(min_token, min(max_tokens, default))

    if OPENAI_API_KEY != "NO_KEY":
        api_key = OPENAI_API_KEY
    else:
        api_key = ""
