import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

# Flask keep_alive server
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your Bot Is Ready"

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()

# --- Discord Bot Setup ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

status = cycle(['with Python', 'GorillaTag'])

@bot.event
async def on_ready():
    await bot.tree.sync()  # sync slash commands (only once, keep here on Replit)
    change_status.start()
    print("✅ Your bot is ready and commands are synced")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# Slash Command (/online)
@bot.tree.command(name="online", description="Check if the bot is online")
async def online(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Yes, I'm online!")

# --- Run Bot ---
keep_alive()
TOKEN = os.environ["DISCORD_TOKEN"]  # Add your bot token in Replit Secrets
bot.run(TOKEN)
