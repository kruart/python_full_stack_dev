from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.title