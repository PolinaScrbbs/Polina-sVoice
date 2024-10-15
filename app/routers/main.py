from quart import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
async def index():
    return await render_template("main/index.html")