FROM --platform=linux/amd64 python:3.8-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]