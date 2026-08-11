from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='orders', null=True, blank=True
    )
    # Shipping Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='United States')

    # Order Info
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order #{self.id} — {self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_address(self):
        return f'{self.address}, {self.city}, {self.state} {self.zip_code}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'store.Product', on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total_price(self):
        return self.price * self.quantity