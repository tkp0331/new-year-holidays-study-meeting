from django.db import models

# Create your models here.


class Faculty(models.Model):
    id = models.IntegerField(verbose_name='学部ID', primary_key=True)
    name = models.CharField(verbose_name='学部名', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Faculties'
