# Generated by Django 3.2 on 2021-05-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
