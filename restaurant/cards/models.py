from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, blank=False, null=True)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title