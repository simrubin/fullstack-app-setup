FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY config.yaml .
COPY .venv/ .venv/

EXPOSE 5000

CMD ["python", ".venv/app.py"]
