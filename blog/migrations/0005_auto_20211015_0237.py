# Generated by Django 3.2.7 on 2021-10-15 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_comments_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auth_comment', to='auth.user'),
            preserve_default=False,
        ),
    ]
