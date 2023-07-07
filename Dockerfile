FROM python:3.9-slim

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Téléchargement du modèle GPT-2
#RUN python -c "from transformers import GPT2Tokenizer, TFGPT2LMHeadModel; tokenizer = GPT2Tokenizer.from_pretrained('gpt2'); model = TFGPT2LMHeadModel.from_pretrained('gpt2')"
COPY saved_model saved_model

COPY *.py ./

COPY static static
COPY templates templates

CMD [ "python", "app.py" ]

EXPOSE 5002