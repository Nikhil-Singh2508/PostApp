from django.db import models

# Create your models here.


class Posts(models.Model):
    user = models.CharField(max_length=200)
    post = models.TextField()

    def __str__(self):
        return {'user': self.user, 'post': self.post}
