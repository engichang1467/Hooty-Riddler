import os
import random
import threading

import discord
import cohere
from dotenv import load_dotenv
import gradio as gr


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
COHERE_TOKEN = os.getenv('COHERE_API_TOKEN')

co = cohere.Client(COHERE_TOKEN)
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Salutation
    if message.content.startswith("Hey Hooty"):
        hooty_salutations = [
            "Hoot Hoot!",
            "Hooty report to duty!"
        ]

        response = random.choice(hooty_salutations)
        await message.channel.send(response)

    if message.content.startswith("Hooty"):
        input_str = message.content
        input_str = input_str.lower()

        # If input contains both "solve" and "riddle"
        if "riddle" in input_str:
            command_prompt = input_str

            response = co.generate(
                  model='command',
                  prompt=command_prompt,
                  max_tokens=260,
                  temperature=0.9,
                  k=0,
                  stop_sequences=[],
                  return_likelihoods='NONE')
    
            response = response.generations[0].text
            await message.channel.send(response)

        else:
            response = "I don't know what you mean, I'm only into riddles"
            await message.channel.send(response)

def run_bot():
    client.run(TOKEN)


threading.Thread(target=run_bot).start()


welcome_message = """
## Add this bot to your server by clicking this link: 
https://discord.com/oauth2/authorize?client_id=1237198809700761640
## How to use it?
- Say Hi to Hooty by typing "Hey Hooty"
- Ask Hooty to give you a riddle by saying something like "Hooty give me a riddle"
- Ask Hooty to solve the riddle by saying something like "Hooty solve this riddle for me please '<input_riddle>'"

This will generate images based on the text prompt. You can upscale the images using the buttons up to 16x!
⚠️ Note ⚠️: Please make sure to type Hooty to get his attention.
⚠️ Note ⚠️: Please make sure the input contain the word "riddle" for Hooty to understand.
"""


with gr.Blocks() as demo:
    gr.Markdown(f"""
    # Hooty the Riddle Assistant
    {welcome_message}
    """)


demo.queue(max_size=100)
demo.launch()
