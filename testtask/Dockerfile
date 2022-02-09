FROM python:3-alpine

ADD . /touch/GenerateFile
WORKDIR /touch/GenerateFile/src

ENTRYPOINT ["python3", "--filename name", "--filesize 128", "-m", "main"]