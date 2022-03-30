FROM python:3.8-slim AS base

RUN mkdir app

RUN pip install poetry
COPY  *.toml *.lock /
COPY kattana_news /app
#COPY setup.py /app
RUN poetry config virtualenvs.create false \
    && poetry install \ 
    && poetry config virtualenvs.create true

WORKDIR /app

#RUN python setup.py install
#CMD ["uvicorn", "--host","0.0.0.0", "--port", "8008","main:app"]
CMD ["python", "main.py"]