from quart import Blueprint, render_template, send_file
from sqlalchemy import select

from ..database import get_session
from ..models.voiceover import Voiceover

history = Blueprint("history", __name__)

@history.route("/history")
async def history_page():

    async with get_session() as session:
        latest_voiceovers = await session.execute(
            select(Voiceover).order_by(Voiceover.id.desc()).limit(5)
        )
        voiceovers = latest_voiceovers.scalars().all()

    return await render_template("history/index.html", voiceovers=voiceovers)

@history.route('/download/<path:filename>')
async def download_file(filename):
    return await send_file(filename , mimetype='audio/mp3', as_attachment=True)