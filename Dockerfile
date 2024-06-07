FROM python:3.9-slim

LABEL maintainer="anshujai4@gmail.com" 

WORKDIR /app

COPY generator.py .

RUN pip install requests

CMD ["python3", "generator.py"]
