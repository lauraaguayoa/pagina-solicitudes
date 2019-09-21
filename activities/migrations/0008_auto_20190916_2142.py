# Generated by Django 2.2.2 on 2019-09-17 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_space_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='space',
        ),
        migrations.AddField(
            model_name='activity',
            name='space',
            field=models.ManyToManyField(blank=True, null=True, to='activities.Space'),
        ),
    ]