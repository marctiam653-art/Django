from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_publication"]

    def __str__(self):
        return self.titre