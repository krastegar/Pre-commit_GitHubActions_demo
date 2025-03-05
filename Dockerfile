FROM python:3.12

WORKDIR /app

COPY src/pre_commit_githubactions_demo/pong.py /app/pong.py

RUN pip install pygame

RUN echo "editiing for the demo purposes"

CMD ["python3", "pong.py"]