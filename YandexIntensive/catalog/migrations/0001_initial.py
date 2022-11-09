# Generated by Django 3.2.16 on 2022-11-09 19:08

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='Макс 150 символов', max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('weight', models.IntegerField(default=100, validators=[catalog.validators.validate_category_weight])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='Макс 150 символов', max_length=150, verbose_name='Название')),
                ('text', models.TextField(help_text='Описание должно быть больше,чем из 2х слов и содержать слова "превосходно, роскошно" ', validators=[catalog.validators.validate_must_be_param], verbose_name='Описание')),
                ('category', models.ForeignKey(help_text='Выберете категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='Макс 150 символов', max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('img', models.ImageField(help_text='Загрузите картинку', null=True, upload_to='preview/%Y/%m', verbose_name='Изображение')),
                ('item', models.OneToOneField(help_text='Выберите товар', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(help_text='Загрузите картинку', upload_to='uploads/%Y/%m', verbose_name='Изображение')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Галлерея',
            },
        ),
    ]
