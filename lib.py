from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
client = OpenAI()


def create_completion(system, user):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return completion.choices[0].message


def create_room(node_text):
    system = """
Create a compelling room description for a text based game.
Use the included context to generate content.
"""
    return create_completion(system, node_text).content


def create_exits(node_text):
    system = """
Create a list of room exits for a text adeventure game.
Use anything wrapped in "[[" and "]]" to create the exits.
Here is an example for [[salami]]. You see an exit towards salami
Return exits in json string format"""
    return create_completion(system, node_text).content


def create_image(room_description):
    return (
        client.images.generate(
            model="dall-e-3", prompt=room_description, n=1, size="1024x1024"
        )
        .data[0]
        .url
    )
