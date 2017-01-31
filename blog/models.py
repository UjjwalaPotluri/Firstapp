from django.db import models
from django.utils import timezone

class post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    test = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate=timezone.now()
        self.save()

    def __str__(self):
        return self.title

