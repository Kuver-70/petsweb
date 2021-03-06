# Generated by Django 3.1.2 on 2020-11-02 07:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets_web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_quantity',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pet',
            name='avatara',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
