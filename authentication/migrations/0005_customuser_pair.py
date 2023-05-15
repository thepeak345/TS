# Generated by Django 4.1.2 on 2023-05-15 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_pair'),
        ('authentication', '0004_customuser_box_customuser_box_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.pair'),
        ),
    ]
