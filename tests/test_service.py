import pytest
import requests


def test_service():
    """RUN docker-compose up before launch"""
    data = '{"text":"@LuckyBartlett We ll be releasing details soon, including for those who held LP tokens, apologies for the delay"}'

    result = requests.post(
        url="http://0.0.0.0:8008/predict",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    assert result.json()["label"] is not None
    # assert result.json()['label'] is not ["technical_update_points"]
