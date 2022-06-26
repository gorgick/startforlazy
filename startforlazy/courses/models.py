from django.db import models
from users.models import Customer
from django.utils import timezone


class Course(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='course')
    name = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Цена курса')
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    vote_amount = models.PositiveIntegerField(default=0, null=True, blank=True)
    vote_ratio = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_reviews(self):
        """Calculate all '+' reviews and make ratio"""
        reviews = self.reviews.all()
        amount_review = reviews.count()
        good_review = reviews.filter(vote='Up').count()
        ratio = (good_review / amount_review) * 100
        self.vote_ratio = ratio
        self.save()

    def reviewers_id_in_review_values(self):
        """Made a list with id's people, who made review"""
        qs = list(self.reviews.values())
        return [el['reviewer_id'] for el in qs]



class Review(models.Model):
    VOTE_RATIO = (
        ('Up', 'good'),
        ('Down', 'bad'),
    )
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    vote = models.CharField(max_length=255, choices=VOTE_RATIO, default='good')
    text = models.TextField(verbose_name='Ваш комментарий', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        unique_together = [['reviewer', 'course']]


class Order(models.Model):
    """Заказ пользователя"""

    STATUS_NEW = 'new'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_COMPLETED, 'Заказ получен покупателем')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='orders', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    start_time = models.TimeField(verbose_name='Время начала занятий')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW)
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата создания заказа', auto_now=True)
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
