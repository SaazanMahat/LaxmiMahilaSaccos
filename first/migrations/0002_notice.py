# Generated by Django 3.0.3 on 2020-04-24 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='posts')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]