from django.db import models # pyright: ignore[reportMissingModuleSource]


class GroceryItem(models.Model):
    CATEGORY_CHOICES = [
        ("Fruit", "Fruit"),
        ("Vegetable", "Vegetable"),
        ("Dairy", "Dairy"),
        ("Meat", "Meat"),
        ("Drink", "Drink"),
        ("Freezer", "Freezer"),
        ("Pantry", "Pantry"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=30)
    date_purchased = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name