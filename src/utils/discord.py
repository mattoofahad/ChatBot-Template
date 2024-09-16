"""Module doc string"""

from discord_webhook import DiscordWebhook

from .config import DISCORD_HOOK
from .logs import logger


def discord_hook(message):
    """_summary_"""
    try:
        logger.info(message)
        url = DISCORD_HOOK
        if url != "NO_HOOK":
            webhook = DiscordWebhook(
                url=url, username="simple-chat-bot", content=message
            )
            webhook.execute()
            logger.debug("Discord Hook Successful.")
        else:
            logger.debug("Discord Hook Failed.")
    except Exception as e:
        logger.error(f"Discord Hook Failed. Error {e}")
