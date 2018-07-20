# Generated by Django 2.0.7 on 2018-07-16 15:13

from django.db import migrations, models
import django.db.models.deletion
import photomanagementapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=photomanagementapp.models.upload_photos, verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photomanagementapp.Gallery')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ('title',),
            },
        ),
    ]