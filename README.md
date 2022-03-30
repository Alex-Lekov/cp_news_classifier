# Service for news classification

## About

------

### Цель проекта

Предоставить клиентам компании автоматическую аналитику новостей.
Аналитика предоставляется в виде установки определенных тегов к каждой ности для того чтобы можно было быстро понять к какому типу относиться данная новость.

### Конечный продукт

Микросервис в докере, который получает по REST API запрос с текстом новости и отдает теги для этой новости.

---------------

## Running Locally Without Docker

Build requirements:

```
python setup.py
```

Run Service:

```
cd kattana_news
python main.py
```

## Building & Running Locally With Docker-Compose

Build the image:

```
docker-compose build
```

Spin up container:

```
docker-compose up
```

---------------

# Road Map

- [x] Model

- [x] WebService

- [x] Docker

- [ ] Logging

- [ ] Docs
