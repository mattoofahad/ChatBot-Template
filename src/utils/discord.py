import os

from discord_webhook import DiscordWebhook

from .config import ENVIRONMENT, DISCORD_HOOK
from .logs import logger

def discord_hook(message):
    """_summary_"""
    if ENVIRONMENT != "LOCAL":
        url = DISCORD_HOOK
        if url != "NO_HOOK":
            webhook = DiscordWebhook(
                url=url, username="simple-chat-bot", content=message
            )
            webhook.execute()
            logger.info("Discord Hook Successful.")
        else:
            logger.info("Discord Hook Failed.")
