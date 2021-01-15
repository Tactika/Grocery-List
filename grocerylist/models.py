from django.db import models

class GroceryList(models.Model):
    description     = models.TextField(max_length=200)
    created_date    = models.DateField(auto_now_add=True)
    purhcased_date  = models.DateField(blank=True, null=True)
    purchased       = models.BooleanField(default=False)

    

