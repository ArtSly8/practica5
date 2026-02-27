from django.db import models

class NameEntry(models.Model):
    # Требование: модель содержит только одно поле "name"
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
