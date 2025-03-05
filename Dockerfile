FROM python:3.12

WORKDIR /app

COPY src/pre_commit_githubactions_demo/pong.py /app/pong.py

RUN pip install pygame

CMD ["python3", "pong.py"]

RUN echo "Press any key to stop and stop the container..."
RUN read -n 1 -s