# Generated by Django 3.2.7 on 2021-10-15 00:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ManyToManyField(related_name='auth_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
