# Generated by Django 3.0 on 2020-04-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_scrollnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrollnews',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
