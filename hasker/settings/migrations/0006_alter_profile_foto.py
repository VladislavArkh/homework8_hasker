# Generated by Django 4.0.6 on 2022-08-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.CharField(max_length=300),
        ),
    ]