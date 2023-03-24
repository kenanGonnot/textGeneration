from flask import Flask, render_template, request, jsonify
from secret_key import OPENAI_API_KEY
import os
import openai
import text_generation

app = Flask(__name__)

openai.api_key = OPENAI_API_KEY


@app.route('/k')
def k():
    return render_template('example.html')


# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route("/", methods=["GET", "POST"])
def generate_text():
    if request.method == "POST":
        # récupérer les paramètres de la requête POST
        text_length = int(request.form['text_length'])
        input_text = request.form['input_text']
        temperature = float(request.form['temperature'])
        which_mode = request.form['model_select']

        # appeler la fonction de génération de texte
        if which_mode == 'gpt2':
            generated_text = text_generation.generate_text_gpt2(text_length, input_text, model_name="gpt2",
                                                                temperature=temperature)
        elif which_mode == 'openai':
            generated_text = text_generation.generate_text_openai(text_length, input_text, model_name="ada",
                                                                  temperature=temperature)
        elif which_mode == 'kenbot':
            # generated_text = text_generation.generate_text_kenbot(text_length, input_text, PATH="model.pt")
            generated_text = "Le modèle Kenbot n'est pas encore disponible"
        else:
            generated_text = "Mode de génération de texte invalide"
        # generated_text.wait()
        # return jsonify({'generated_text': generated_text})
        return render_template('home.html', generated_text=input_text + " " + generated_text)
    else:
        return render_template('home.html')


# renvoyer le texte généré à la page HTML


# else:
#     return render_template('home.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
