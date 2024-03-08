FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/finz

COPY ./Pipfile ./

RUN pip install pipenv && pipenv lock && pipenv requirements > requirements.txt

RUN rm -f ./Pipfile ./Pipfile.lock

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]