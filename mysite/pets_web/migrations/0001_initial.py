# Generated by Django 3.1.2 on 2020-10-28 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.DateField()),
                ('breed', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('avatara', models.ImageField(upload_to='')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_kind', models.CharField(choices=[('Котейка', 'Котейка'), ('Собакен', 'Собакен'), ('Морская свинка', 'Морская свинка'), ('Хомяк', 'Хомяк'), ('Рыбка', 'Рыбка')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes_quantity', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets_web.pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets_web.petkind'),
        ),
    ]
