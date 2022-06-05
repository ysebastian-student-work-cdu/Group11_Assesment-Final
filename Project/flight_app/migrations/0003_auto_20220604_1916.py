# Generated by Django 3.0.3 on 2022-06-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_app', '0002_auto_20220604_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='city',
            new_name='PassportNumber',
        ),
        migrations.RemoveField(
            model_name='book',
            name='country',
        ),
        migrations.RemoveField(
            model_name='book',
            name='state_province',
        ),
        migrations.AlterField(
            model_name='book',
            name='website',
            field=models.URLField(default='any y'),
        ),
    ]
