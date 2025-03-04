FROM python:3.12

WORKDIR /app

COPY pong.py /app/pong.py
COPY main.py /app/main.py

RUN pip install pygame

CMD ["python", "pong.py"]