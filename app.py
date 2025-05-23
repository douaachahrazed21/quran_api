# Le cœur de l'API Flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from inference import transcrire_et_comparer
import os
import tempfile

app = Flask(__name__)
CORS(app)

@app.route("/transcrire", methods=["POST"])
def transcrire():
    if 'audio' not in request.files:
        return jsonify({"error": "Aucun fichier audio fourni."}), 400

    sourate = request.form.get("sourate")
    debut = request.form.get("debut")
    fin = request.form.get("fin")

    if not (sourate and debut and fin):
        return jsonify({"error": "Champs manquants : sourate, debut, fin"}), 400

    audio = request.files['audio']
    
    temp_dir = tempfile.gettempdir()
    audio_path = f"{temp_dir}/{audio.filename}"
    audio.save(audio_path)

    result = transcrire_et_comparer(audio_path, int(sourate), int(debut), int(fin))

    os.remove(audio_path)
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
