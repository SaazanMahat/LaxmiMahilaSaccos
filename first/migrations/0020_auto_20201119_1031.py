# Generated by Django 3.0.3 on 2020-11-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0019_auto_20201119_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='yearly_interest_rate',
            new_name='traimasik_interest_rate',
        ),
    ]
