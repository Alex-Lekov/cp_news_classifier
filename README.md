# Service for news classification

## About

------

### Цель проекта

Предоставить клиентам компании автоматическую аналитику новостей.
Аналитика предоставляется в виде установки определенных тегов к каждой ности для того чтобы можно было быстро понять к какому типу относиться данная новость.

### Конечный продукт

Микросервис в докере, который получает по REST API запрос с текстом новости и отдает теги для этой новости.

## API

Через Post запрос на порт 8008 отправляем текст, в ответ получаем лист из тегов и текст

Пример:

```python
import requests
text = '{"text":"@LuckyBartlett We ll be releasing details soon, including for those who held LP tokens, apologies for the delay"}'

result = requests.post(
    url="http://0.0.0.0:8008/predict",
    data=text,
    headers={"Content-Type": "application/json"},
    )
print(result.json())
```

Результат:

```
{'text': '@LuckyBartlett We ll be releasing details soon, including for those who held LP tokens, apologies for the delay',
 'label': ['technical_update_points']}
```

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
