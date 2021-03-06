# Generated by Django 4.0.4 on 2022-05-30 14:06

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Open_lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('additional', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('slug_register', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('phota', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_of_the_event', models.DateTimeField()),
                ('spiker', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('for_information', models.CharField(max_length=30)),
                ('published', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_lessons.author_register')),
                ('categories', models.ManyToManyField(to='open_lessons.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_lessons.open_lessons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
