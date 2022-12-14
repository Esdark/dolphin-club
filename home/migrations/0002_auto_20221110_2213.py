# Generated by Django 3.2 on 2022-11-10 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeMaster',
            fields=[
                ('ageid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('position', models.IntegerField(default=1)),
                ('hide', models.CharField(default='N', max_length=1)),
                ('Datemodified', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'AGEMASTER',
            },
        ),
        migrations.CreateModel(
            name='MaterialMaster',
            fields=[
                ('materialid', models.AutoField(primary_key=True, serialize=False)),
                ('materialname', models.CharField(max_length=100)),
                ('position', models.IntegerField(default=1)),
                ('hide', models.CharField(default='N', max_length=1)),
                ('Datemodified', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'MATERIALMASTER',
            },
        ),
        migrations.DeleteModel(
            name='GalleryPageMaster',
        ),
    ]
