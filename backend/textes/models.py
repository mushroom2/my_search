from django.db import models
from django.db.models import TextField, DateTimeField, ForeignKey, FloatField, CASCADE
from django.contrib.postgres.fields import ArrayField


class RawText(models.Model):
    raw_content = TextField()
    created_at = DateTimeField(auto_now=True)


class Sentence(models.Model):
    content = TextField()
    text = ForeignKey(RawText, on_delete=CASCADE, related_name='sentences')
    vectors = ArrayField(FloatField(), default=list)
