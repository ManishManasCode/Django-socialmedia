# Generated by Django 4.2.2 on 2023-06-10 06:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_userpostsmodel_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpostsmodel',
            old_name='descripition',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='userpostsmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_post_model_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]