# Generated by Django 3.2 on 2021-05-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('completed', models.BooleanField()),
                ('url', models.CharField(max_length=500)),
                ('order', models.IntegerField()),
            ],
        ),
    ]
