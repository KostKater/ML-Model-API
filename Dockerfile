FROM python:3.9-slim

RUN mkdir app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD uvicorn main:app --port=80 --host=0.0.0.0