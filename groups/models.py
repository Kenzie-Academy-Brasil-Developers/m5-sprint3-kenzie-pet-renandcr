from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Group {self.id} - {self.name}"
