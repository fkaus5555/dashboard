# Generated by Django 3.0.7 on 2020-06-18 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200618_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='date',
        ),
    ]
