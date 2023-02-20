# Service for news classification 
use DeepLearning models and FastAPI

## About

------

### Project goal

Provide the company's clients with automatic news analytics.
Analytics is provided in the form of setting specific tags for each news item so that you can quickly understand what type of news this news belongs to.

### Final product

Microservice in docker, which receives a REST API request with the text of the news and gives tags for this news.

## API

We send a text via a Post request to port 8008, in response we receive a sheet of tags and text

Example:

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

Result:

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
