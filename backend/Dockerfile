FROM python:3.12-slim-bullseye

RUN apt-get update && \
    apt-get install -y libcairo2-dev pkg-config build-essential ffmpeg libsm6 libxext6 git tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml .

RUN pip install uv

RUN uv sync

COPY . .

EXPOSE 8001

ENV PYTHONPATH=/app

CMD ["uv", "run", "main.py"]
