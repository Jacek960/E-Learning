from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify
from tinymce import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=250)
    category_description = models.TextField(blank=True, null=True)
    category_img = models.ImageField(upload_to='category_image/', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name.lower().replace('ł', 'l'))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


COURSE_TYPES = (
    (0, "Free"),
    (1, "Premium")
)


class Course(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=250)
    content = HTMLField('Content')
    time_stamp = models.DateTimeField(auto_now_add=True)
    course_img = models.ImageField(upload_to='course_image/', blank=True, null=True)
    course_type = models.IntegerField(choices=COURSE_TYPES, default=0)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name.lower().replace('ł', 'l'))
        super(Course, self).save(*args, **kwargs)

    def cours_content_short(self):
        return self.content[0:240]

    def __str__(self):
        return f'{self.category} - {self.name}'


class Banner(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='baner/')
    url = models.CharField(max_length=350, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Premium(models.Model):
    name = models.CharField(max_length=64)
    no_of_days = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Premium, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}-{self.product}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Premium, on_delete=models.SET_NULL, null=True)
    premium = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}-{self.product}------premium status {self.premium}'


def create_profile(sender, user, request, **kwargs):
    Profile.objects.get_or_create(user=user)


user_logged_in.connect(create_profile)
