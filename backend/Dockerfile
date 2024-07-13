FROM python:3.8-slim-buster

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN export PYTHONPATH=.
CMD ["python3", "-m", "flask", "--app", "./src/main:app", "run", "--host=0.0.0.0", "--port=8002"]
