from quart import Blueprint, render_template, request, send_file
from ..voiceover import to_voice
from ..database import get_session
from ..models.voiceover import Voiceover

converter = Blueprint("converter", __name__)

@converter.route("/converter")
async def converter_page():
    return await render_template("converter/index.html")

@converter.route('/converter', methods=['POST'])
async def convert():
    form_data = await request.form
    text = form_data.get('text', '').strip()
    
    if not text or len(text) > 256:
        return {"error": "The text must contain from 1 to 256 characters."}, 400
    
    audio_file_path  = await to_voice(text)
    async with get_session() as session:
        new_voiceover = Voiceover(text=text, voceover_path=audio_file_path)
        session.add(new_voiceover)
        await session.commit()
    
    return await send_file(audio_file_path , mimetype='audio/mp3', as_attachment=True)