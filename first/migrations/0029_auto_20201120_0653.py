# Generated by Django 3.0.3 on 2020-11-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0028_auto_20201119_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
