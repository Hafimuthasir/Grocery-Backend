from django.db import models

class GroceryItem(models.Model):
    CATEGORY_CHOICES = [
        ('produce', 'Produce'),
        ('dairy', 'Dairy'),
        ('meat', 'Meat'),
        ('grains', 'Grains'),
        ('canned_goods', 'Canned Goods'),
        ('fruits', 'Fruits'),
    ]

    UNIT_CHOICE = [
        ('kgs', 'Kgs'),
        ('grams', 'Grams'),
        ('liters', 'Liters'),
        ('number', 'Number')
    ]

    name = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICE)

    def __str__(self):
        return self.name
