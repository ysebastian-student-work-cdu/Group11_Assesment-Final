# Generated by Django 3.0.3 on 2022-06-04 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight_app', '0003_auto_20220604_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='website',
        ),
        migrations.AddField(
            model_name='book',
            name='DepartureDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Destination',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='ReturnDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
