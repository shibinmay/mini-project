# Generated by Django 5.0.6 on 2024-06-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_home_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='place',
            new_name='Place',
        ),
        migrations.AddField(
            model_name='home',
            name='Age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]