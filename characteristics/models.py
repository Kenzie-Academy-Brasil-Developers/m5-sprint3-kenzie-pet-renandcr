from django.db import models

class Characteristic(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return f"Characteristic {self.id} - {self.name}"
