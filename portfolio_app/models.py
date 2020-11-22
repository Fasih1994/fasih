from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_url = models.URLField()
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title