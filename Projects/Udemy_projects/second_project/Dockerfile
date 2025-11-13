FROM python:3.9.0-alpine

#choose the directory
WORKDIR /srv/app

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY ./requirement.txt /srv/app/

RUN pip install --no-cache-dir  -r requirement.txt

COPY . /srv/app/

CMD ["uvicorn", "books2:app", "--host", "0.0.0.0", "--port", "8091"]



