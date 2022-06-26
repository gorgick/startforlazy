from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    image_user = models.ImageField(default='users/user-default.png', upload_to='users/', null=True, blank=True,
                                   verbose_name='Ваше фото')
    customer_orders = models.ManyToManyField(to='courses.Order', blank=True, related_name='related_customer')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
