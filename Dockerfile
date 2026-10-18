FROM python:3.13-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY configs/ configs/
COPY data/sample/ data/sample/
RUN mkdir -p results
CMD ["python", "src/benchmark.py", "--config", "configs/config.json"]
