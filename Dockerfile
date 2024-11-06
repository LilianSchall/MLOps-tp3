FROM python:3.11-slim-bullseye

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./wsgi.py .
COPY ./server/ ./server
EXPOSE 8000

ENTRYPOINT [ "gunicorn", "-w", "4", "wsgi:app", "-b", "0.0.0.0:8000", "--log-level=debug" ]
