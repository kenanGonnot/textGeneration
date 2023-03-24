FROM python:3.9-slim

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
#RUN python -m spacy download en_core_web_sm
COPY *.py ./

COPY templates templates

CMD [ "python", "app.py" ]

EXPOSE 5000