from django.db import models

class FormView(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    ico = models.CharField(blank=False,max_length=8)

    def __str__(self):
        return self.name