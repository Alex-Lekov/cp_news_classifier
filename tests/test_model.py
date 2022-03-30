import pytest
from itertools import compress
from kattana_news.model import Model


def test_model():
    TEGS = [
        "release_points",
        "technical_update_points",
        "partnership_points",
        "listing_points",
        "security_points",
        "from_the_project",
        "not_from_the_project",
        "staking",
    ]
    text = "@LuckyBartlett We ll be releasing details soon, including for those who held LP tokens, apologies for the delay"

    model = Model(file_model_name="kattana_news/model.h5")
    predict_probas = model.predict_proba(text)
    text_tegs = list(compress(TEGS, (model.predict_proba(text) > 0.5)[0]))

    assert predict_probas is not None
    assert text_tegs is not None
    assert len(text_tegs) > 0
    # assert text_tegs is not ["technical_update_points"]
