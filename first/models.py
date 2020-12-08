import random
import string
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()


class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='notices', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date_posted"]


class Slideshow(models.Model):
    content = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='slideshow', blank=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('homepage', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Slideshow, self).save(*args, **kwargs)


class ScrollNews(models.Model):
    content = models.CharField(max_length=1000)

    def __str__(self):
        return "scrollnews"

    def get_absolute_url(self):
        return reverse('homepage', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.pk and ScrollNews.objects.exists():
            raise ValidationError(
                'There is can be only one ScrollNews instance')
        return super(ScrollNews, self).save(*args, **kwargs)


class Image(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='image_main')
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


class Video(models.Model):
    Video_Description = models.CharField(max_length=500)
    videofile = models.FileField(
        upload_to='videos/', null=True, verbose_name="")
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.Video_Description

    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)


class Report(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='reports/', null=True, verbose_name="")
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Form(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='forms/', null=True, verbose_name="")
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Statistic(models.Model):

    total_share_capital = models.CharField(max_length=500)
    total_institutional_capital = models.CharField(max_length=500)
    total_saving = models.CharField(max_length=500)
    total_assets = models.CharField(max_length=500)
    total_loan = models.CharField(max_length=500)
    total_members = models.CharField(max_length=500)
    total_employees = models.CharField(max_length=500)
    data_updated_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('homepage', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.pk and Statistic.objects.exists():
            raise ValidationError('There is can be only one instance')
        return super(Statistic, self).save(*args, **kwargs)

    def __str__(self):
        return "Edit this"


class PopUp(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='popup')
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


def generate_unique_code_loan():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Loan.objects.filter(code=code).count() == 0:
            break
    return code


def generate_unique_code_saving():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Saving.objects.filter(code=code).count() == 0:
            break
    return code


def generate_unique_code_other():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Other_program.objects.filter(code=code).count() == 0:
            break
    return code


class Loan(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(
        max_length=8, default=generate_unique_code_loan, unique=True, null=True, blank=True)
    main_text = models.CharField(max_length=250, null=True)
    image = models.FileField(upload_to='loans_images', null=True)
    amount = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    monthly_interest_rate = models.CharField(max_length=100)
    traimasik_interest_rate = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Saving(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(
        max_length=8, default=generate_unique_code_saving, unique=True, null=True, blank=True)
    interest_rate = models.CharField(max_length=100)
    image = models.FileField(upload_to='savings_images', null=True)

    def __str__(self):
        return self.title


class Other_program(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(
        max_length=8, default=generate_unique_code_other, unique=True, null=True, blank=True)
    main_text = models.CharField(max_length=1000)
    image = models.FileField(upload_to='otherprograms_images', null=True)

    def __str__(self):
        return self.title
