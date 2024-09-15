FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run_app.py"]

EXPOSE 5000
EXPOSE 8501

