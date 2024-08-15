"""Module doc string"""

from discord_webhook import DiscordWebhook

from .config import DISCORD_HOOK, ENVIRONMENT
from .logs import logger


def discord_hook(message):
    """_summary_"""
    logger.info(message)
    if ENVIRONMENT != "LOCAL":
        url = DISCORD_HOOK
        if url != "NO_HOOK":
            webhook = DiscordWebhook(
                url=url, username="simple-chat-bot", content=message
            )
            webhook.execute()
            logger.debug("Discord Hook Successful.")
        else:
            logger.debug("Discord Hook Failed.")
