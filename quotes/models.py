from django.db import models

class Source(models.Model):
    SOURCE_TYPE_CHOICES = [
        ('movie', 'Фильм'),
        ('book', 'Книга'),
        ('series', 'Сериал'),
        ('other', 'Другое'),
    ]
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=SOURCE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField(unique=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='quotes')
    weight = models.PositiveIntegerField(default=1, help_text="Чем выше — тем чаще показывается")
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text[:50]}..." — {self.source.name}'
