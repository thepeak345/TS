# Generated by Django 4.1.2 on 2023-02-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
