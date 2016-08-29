from django.db import models

class Articles(models.Model):

    titre = models.CharField(max_length=100)

    soustitre = models.CharField(max_length=100)

    auteur = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    contenu = models.TextField(null=True)

    date = models.DateTimeField(auto_now_add=True, auto_now=False, 

                                verbose_name="Date de parution")
    def __str__(self):
        return self.titre
