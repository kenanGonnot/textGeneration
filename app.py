import json

from flask import Flask, render_template, request, jsonify
from secret_key import OPENAI_API_KEY
import os
import openai
import text_generation

app = Flask(__name__)

openai.api_key = OPENAI_API_KEY

error_message = {
    "error_message": "error"
}

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/v1/text_generation", methods=["GET", "POST"])
def generate_text():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        data = json.loads(data)
        text_length = int(data['text_length'])
        input_text = data['input_text']
        temperature = float(data['temperature'])
        which_mode = data['model_select']

        input_text, text_generated = get_text_generated(input_text, temperature, text_length, which_mode)
        # generated_text.wait()
        # return jsonify({'generated_text': generated_text})
        response = {
            "text_length": text_length,
            "input_text": input_text,
            "temperature": temperature,
            "model_select": which_mode,
            "text_generated": text_generated
        }
        return jsonify(response)
        # return render_template('home.html', generated_text=input_text + " " + text_generated)
    else:
        return jsonify(error_message)
        # return render_template('home.html')


def get_text_generated(input_text, temperature, text_length, which_mode):
    # appeler la fonction de génération de texte
    if which_mode == 'gpt2':
        text_generated = text_generation.generate_text_gpt2(text_length, input_text, model_name="gpt2",
                                                            temperature=temperature)
        input_text = ''
    elif which_mode == 'openai':
        text_generated = text_generation.generate_text_openai(text_length, input_text, model_name="ada",
                                                              temperature=temperature)
    elif which_mode == 'kenbot':
        text_generated = text_generation.generate_text_kenbot(text_length, input_text,
                                                              PATH="./saved_model/saved-tiktoken-64batch-128block-255440-ite-x_xx")
        # generated_text = "Le modèle Kenbot n'est pas encore disponible"
        input_text = ''
    else:
        text_generated = "Mode de génération de texte invalide"
    return input_text, text_generated


# Route pour la page d'erreur 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5002))
    app.run(debug=True, host='0.0.0.0', port=port)
