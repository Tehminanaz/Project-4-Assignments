import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a bot instance with necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Enables access to message content

bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="Fun with Tehmina! 🎉"))

# Event to respond when a message is sent
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return
    
    # Respond to the keyword "Tehmina"
    if message.content.lower() == "Tehmina":
        responses = [
            "Hello! I'm Tehmina, your friendly bot! 👋",
            "You called? How can I help you today? 😊",
            "Tehmina at your service! Type !help to see what I can do!",
            "Hey there! Need something? Try one of my commands!",
            "Tehmina here! Ready for some fun? Try !riddle or !fact!"
        ]
        await message.channel.send(random.choice(responses))
    
    # Process commands (important to keep command functionality working)
    await bot.process_commands(message)

# Error handler for all commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("🚫 Command not found! Try `!ping`, `!hello`, `!riddle`, `!flip`, `!rps`, `!fact`, or `!clear`.")
    else:
        await ctx.send("⚠️ An error occurred.")
        print(f"Error: {error}")

# Ping command to check bot responsiveness
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🎣")

# Greet user with their name
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}! 😊")

# Coin flip command
@bot.command()
async def flip(ctx):
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await ctx.send(f"The coin landed on: {result}")

# Rock-Paper-Scissors Game
@bot.command()
async def rps(ctx, choice: str):
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)

    if choice.lower() not in options:
        await ctx.send("❌ Invalid choice! Choose rock, paper, or scissors.")
        return

    # Determine the winner
    result = "It's a tie! 😐" if choice.lower() == bot_choice else \
             "You win! 🎉" if (choice.lower() == "rock" and bot_choice == "scissors") or \
                            (choice.lower() == "paper" and bot_choice == "rock") or \
                            (choice.lower() == "scissors" and bot_choice == "paper") else \
             "I win! 😎"

    await ctx.send(f"Your choice: {choice.capitalize()} | My choice: {bot_choice.capitalize()} \n{result}")

# Riddle game command
riddles = {
    "What has to be broken before you can use it?": "egg",
    "The more of me you take, the more you leave behind. What am I?": "footsteps",
    "What can't talk but will reply when spoken to?": "echo"
}

@bot.command()
async def riddle(ctx):
    question, answer = random.choice(list(riddles.items()))
    await ctx.send(f"🤔 Riddle: {question}")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        if msg.content.lower() == answer:
            await ctx.send("✅ Correct! 🎉")
        else:
            await ctx.send(f"❌ Wrong! The correct answer was: **{answer}**")
    except:
        await ctx.send(f"⏳ Time's up! The answer was: **{answer}**")

# Fun facts command
facts = [
    "Honey never spoils. Archaeologists found 3000-year-old honey and it was still good! 🍯",
    "Octopuses have three hearts! ❤️❤️❤️",
    "Bananas are berries, but strawberries aren't! 🍌",
    "A day on Venus is longer than a year on Venus. 🌍"
]

@bot.command()
async def fact(ctx):
    await ctx.send(f"📜 Did you know? {random.choice(facts)}")

# Word scramble game
words = ["python", "discord", "bot", "coding", "developer"]

@bot.command()
async def scramble(ctx):
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    await ctx.send(f"🔀 Unscramble this word: `{scrambled}`")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        if msg.content.lower() == word:
            await ctx.send("✅ Correct! 🎉")
        else:
            await ctx.send(f"❌ Wrong! The correct word was: **{word}**")
    except:
        await ctx.send(f"⏳ Time's up! The word was: **{word}**")

# Command to clear messages from the chat
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    """Clears the specified number of messages"""
    if amount <= 0:
        await ctx.send("❌ Please specify a positive number of messages to delete.")
        return
    
    try:
        deleted = await ctx.channel.purge(limit=amount + 1)  # Includes the command itself
        confirmation = await ctx.send(f"🧹 Deleted {len(deleted) - 1} messages.")
        
        import asyncio
        await asyncio.sleep(5)
        await confirmation.delete()
    except discord.errors.HTTPException as e:
        if e.code == 50034:  # Messages older than 14 days
            await ctx.send("❌ Cannot delete messages older than 14 days due to Discord limitations.")
        else:
            await ctx.send(f"❌ Error: {e}")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

# Specific error handler for clear command
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Please provide a valid number.")
    else:
        await ctx.send("⚠️ An error occurred while trying to clear messages.")
        print(f"Clear command error: {error}")

# Run the bot using the token from .env
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN not found! Check your .env file.")

bot.run(TOKEN)
