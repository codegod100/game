import lib
from flask import Flask, render_template

app = Flask(__name__)

example_node = """
# Dust Theory

- a [[theory]]
	- by [[greg egan]]
		- in [[permutation city]]
		- properly called [[dust universe theory]]
	- #go https://www.gregegan.net/PERMUTATION/FAQ/FAQ.html
"""


@app.route("/")
def hello_world():
    description = lib.create_room(example_node)
    return render_template(
        "room.html",
        description=description,
        exits=lib.create_exits(example_node),
        image_url=lib.create_image(description[:1000]),
    )
