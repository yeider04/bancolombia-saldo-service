FROM python:3.9-slim
WORKDIR /app
COPY saldo.py /app/
CMD ["python", "saldo.py"]