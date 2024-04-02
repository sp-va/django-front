import uuid

from django.db import models


class TimeMixin(models.Model):
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(TimeMixin):
    id: models.UUIDField = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title: models.CharField = models.CharField(unique=True, max_length=50)
    text: models.TextField = models.TextField()

    def __str__(self):
        return self.title


class Feedback(TimeMixin):
    id: models.UUIDField = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email: models.EmailField = models.EmailField()
    message: models.TextField = models.TextField()
