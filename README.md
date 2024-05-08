# <img src="img/Hooty_Face.jpeg" width="120px" alt="SFU Surge logo" /> Hooty the Riddle Assistant

This is Hooty and he loves riddles. You can ask him for riddles and solutions too.

You can invite him into your discord server [here](https://discord.com/oauth2/authorize?client_id=1237198809700761640)

**Warning**: Deployment is still a little inconsistent from calling discord API, I'll have to restart the huggingface space multiple times.

## To run the bot locally

- Install everything from the `requirements.txt`

```
pip install -r requirements.txt
```

- Run the code
```
python app.py
```

## How it works?

- Using Discord API to integrate with the Discord app
- Using Cohere API to retrieve input and generate riddles
- Using HuggingFace Space to deploy Hooty

## Demo

![](img/Hooty-discord-demo.gif)