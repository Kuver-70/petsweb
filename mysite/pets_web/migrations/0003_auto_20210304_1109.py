# Generated by Django 3.1.2 on 2021-03-04 04:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets_web', '0002_auto_20201102_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
