import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file (like the bot token)
load_dotenv()

# Set up bot intents (what the bot is allowed to listen to)
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Create bot instance with a prefix for commands
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready and online
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="Fun with Tehmina! 🎉"))

# Event: When a message is sent in any channel
@bot.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == bot.user:
        return
    
    # Respond if someone types "Tehmina"
    if message.content.lower() == "Tehmina":
        responses = [
            "Hello! I'm Humo, your friendly bot! 👋",
            "You called? How can I help you today? 😊",
            "Humo at your service! Type !help to see what I can do!",
            "Hey there! Need something? Try one of my commands!",
            "Humo here! Ready for some fun? Try !riddle or !fact!"
        ]
        await message.channel.send(random.choice(responses))
    
    # Process commands after handling custom messages
    await bot.process_commands(message)

# Error Handler: When command fails or doesn't exist
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("🚫 Command not found! Try `!ping`, `!hello`, `!riddle`, `!flip`, `!rps`, `!fact`, or `!clear`.")
    else:
        await ctx.send("⚠️ An error occurred.")
        print(f"Error: {error}")

# !ping command - Responds with Pong!
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🎣")

# !hello command - Greets the user
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}! 😊")

# !flip command - Flips a coin
@bot.command()
async def flip(ctx):
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await ctx.send(f"The coin landed on: {result}")

# !rps command - Rock, Paper, Scissors game
@bot.command()
async def rps(ctx, choice: str):
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)

    if choice.lower() not in options:
        await ctx.send("❌ Invalid choice! Choose rock, paper, or scissors.")
        return

    # Determine result
    result = "It's a tie! 😐" if choice.lower() == bot_choice else \
             "You win! 🎉" if (choice.lower() == "rock" and bot_choice == "scissors") or \
                            (choice.lower() == "paper" and bot_choice == "rock") or \
                            (choice.lower() == "scissors" and bot_choice == "paper") else \
             "I win! 😎"

    await ctx.send(f"Your choice: {choice.capitalize()} | My choice: {bot_choice.capitalize()} \n{result}")

# Dictionary of riddles and answers
riddles = {
    "What has to be broken before you can use it?": "egg",
    "The more of me you take, the more you leave behind. What am I?": "footsteps",
    "What can't talk but will reply when spoken to?": "echo"
}

# !riddle command - Sends a riddle and waits for answer
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

# List of fun facts
facts = [
    "Honey never spoils. Archaeologists found 3000-year-old honey and it was still good! 🍯",
    "Octopuses have three hearts! ❤️❤️❤️",
    "Bananas are berries, but strawberries aren't! 🍌",
    "A day on Venus is longer than a year on Venus. 🌍"
]

# !fact command - Sends a random fact
@bot.command()
async def fact(ctx):
    await ctx.send(f"📜 Did you know? {random.choice(facts)}")

# Word list for scramble game
words = ["python", "discord", "bot", "coding", "developer"]

# !scramble command - Unscramble game
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

# !clear command - Deletes a number of messages
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    """Clear any specified number of messages from the channel"""
    if amount <= 0:
        await ctx.send("❌ Please specify a positive number of messages to delete.")
        return
    
    try:
        deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to also delete the command message
        confirmation = await ctx.send(f"🧹 Deleted {len(deleted) - 1} messages.")
        
        # Wait 5 seconds before deleting the confirmation message
        import asyncio
        await asyncio.sleep(5)
        await confirmation.delete()
    except discord.errors.HTTPException as e:
        if e.code == 50034:  # Can't delete messages older than 14 days
            await ctx.send("❌ Cannot delete messages older than 14 days due to Discord limitations.")
        else:
            await ctx.send(f"❌ Error: {e}")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

# Error handler for clear command
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Please provide a valid number.")
    else:
        await ctx.send("⚠️ An error occurred while trying to clear messages.")
        print(f"Clear command error: {error}")

# Get bot token from environment variable
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN not found! Check your .env file.")

# Run the bot
bot.run(TOKEN)
