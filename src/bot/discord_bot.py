import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@tree.command(
    name="validate",
    description="Validate CSV roster file"
)
async def validate_command(interaction: discord.Interaction, file: discord.Attachment):
    await interaction.response.send_message("Hello!")


@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")


def run():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")

    if TOKEN is None:
        raise ValueError("DISCORD_BOT_TOKEN not found in environment")

    client.run(TOKEN)
