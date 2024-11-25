# Generated by Django 4.0.6 on 2022-07-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_header', models.CharField(max_length=500)),
                ('question_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]