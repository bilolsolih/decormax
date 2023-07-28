# Generated by Django 4.2.1 on 2023-07-23 01:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_de', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
                ('subtitle_en', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
                ('subtitle_de', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
                ('subtitle_uz', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
                ('photo', models.ImageField(upload_to='images/news/%Y/%m/%d', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('content_en', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_de', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('photo', models.ImageField(upload_to='images/news/%Y/%m/%d', verbose_name='Photo')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='news.news', verbose_name='News')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
    ]
