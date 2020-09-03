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
        return self.content[0:20]

    def __str__(self):
        return f'{self.category} - {self.name}'




