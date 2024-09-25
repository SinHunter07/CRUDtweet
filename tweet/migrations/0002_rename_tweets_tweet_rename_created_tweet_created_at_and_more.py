# Generated by Django 5.1.1 on 2024-09-20 18:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Tweet',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='updated',
            new_name='updated_at',
        ),
    ]