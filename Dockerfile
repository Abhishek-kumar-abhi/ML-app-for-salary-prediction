FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE ${PORT}
CMD gunicorn --bind 0.0.0:${PORT} app:app