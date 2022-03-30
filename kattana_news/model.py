"""
    Model functions and Class
"""

########################## IMPORT ###############################
import numpy as np

# Then what you need from tensorflow.keras
from tensorflow.keras.models import load_model
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
from transformers import DistilBertConfig, DistilBertTokenizerFast

import tensorflow as tf
import tensorflow_addons as tfa

########################## FUNC ###############################


def multi_label_accuracy(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    """For multi-label classification, one has to define a custom
    acccuracy function because neither tf.keras.metrics.Accuracy nor
    tf.keras.metrics.CategoricalAccuracy evaluate the number of
    exact matches.

    :Example:
    >>> from tensorflow.keras import metrics
    >>> y_true = tf.convert_to_tensor([[1., 1.]])
    >>> y_pred = tf.convert_to_tensor([[1., 0.]])
    >>> metrics.Accuracy()(y_true, y_pred).numpy()
    0.5
    >>> metrics.CategoricalAccuracy()(y_true, y_pred).numpy()
    1.0
    >>> multi_label_accuracy(y_true, y_pred).numpy()
    0.0
    """
    y_pred = tf.math.round(y_pred)
    exact_matches = tf.math.reduce_all(y_pred == y_true, axis=1)
    exact_matches = tf.cast(exact_matches, tf.float32)
    return tf.math.reduce_mean(exact_matches)


class Model(object):
    """
    main model class, loading weights and predict
    """

    def __init__(
        self,
        file_model_name: str = "model.h5",
        max_length: int = 50,
        model_name: str = "distilbert-base-uncased",
    ) -> None:
        """
        Args:
            file_model_name (str, optional): file name. Defaults to "model.h5".
            max_length (int, optional): max_length tokens. Defaults to 50.
            model_name (str, optional): model name. Defaults to "distilbert-base-uncased".
        """
        config = DistilBertConfig.from_pretrained(model_name)
        self.model = load_model(
            file_model_name,
            custom_objects={
                "multi_label_accuracy": multi_label_accuracy,
                "RectifiedAdam": tfa.optimizers.RectifiedAdam,
            },
        )

        self.tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
        self.max_length = max_length

    def predict_proba(self, text: str = "sample of sample") -> np.array:
        """
        Probability estimates.
        The returned estimates for all classes are ordered by the
        label of classes.

        Args:
            text (str): text for predict

        Returns:
            List[float]: Returns the probability of the sample for each class in the model
        """
        padded_encodings = self.tokenizer.encode_plus(
            text,
            max_length=self.max_length,  # truncates if len(s) > max_length
            return_token_type_ids=True,
            return_attention_mask=True,
            truncation=True,
            padding="max_length",
            return_tensors="tf",
        )

        predict_probas = self.model(padded_encodings["input_ids"]).numpy()
        return predict_probas
