# Generated by Django 3.1.1 on 2020-10-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='learnings',
            field=models.CharField(default='Some String', max_length=200),
        ),
    ]
