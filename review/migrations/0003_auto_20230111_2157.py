# Generated by Django 3.2.15 on 2023-01-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]