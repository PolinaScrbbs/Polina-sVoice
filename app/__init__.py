import asyncio
from quart import Quart

from .routers.main import main
from .routers.converter import converter
from .routers.history import history

async def create_app() -> Quart:
    app = Quart(__name__)

    app.register_blueprint(main)
    app.register_blueprint(converter)
    app.register_blueprint(history)

    return app

app = asyncio.run(create_app())

