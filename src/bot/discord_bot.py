import discord
import os
from dotenv import load_dotenv
import tempfile
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@tree.command(
    name="validate",
    description="Validate CSV roster file"
)
async def validate_command(interaction: discord.Interaction, file: discord.Attachment):
    command_name = interaction.command.name if interaction.command else "unknown"
    logger.info(
        f"Received `{command_name}` command from {interaction.user.name}")
    await interaction.response.send_message("File received. Report will be ready soon...")


@client.event
async def on_ready():
    await tree.sync()
    logger.info(f"We have logged in as {client.user}")


def run():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")

    if TOKEN is None:
        raise ValueError("DISCORD_BOT_TOKEN not found in environment")
    else:
        logger.info("Token is identified")

    client.run(TOKEN)
