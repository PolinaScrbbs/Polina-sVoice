from quart import Blueprint, render_template, request, send_file
from ..voiceover import to_voice

converter = Blueprint("converter", __name__)

@converter.route("/converter")
async def converter_page():
    return await render_template("converter/index.html")

@converter.route('/converter', methods=['POST'])
async def convert():
    form_data = await request.form
    text = form_data.get('text', '')
    
    audio_file = await to_voice(text)
    
    return await send_file(audio_file, mimetype='audio/mp3', as_attachment=True)