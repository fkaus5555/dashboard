# Generated by Django 3.0.7 on 2020-06-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200618_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='link',
        ),
        migrations.AddField(
            model_name='stockdata',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]