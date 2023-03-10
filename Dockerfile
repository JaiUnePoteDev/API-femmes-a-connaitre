FROM python:3-slim-buster

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]