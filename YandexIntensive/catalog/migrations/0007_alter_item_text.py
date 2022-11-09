# Generated by Django 3.2.16 on 2022-11-09 20:43

import catalog.validators
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=tinymce.models.HTMLField(help_text='Описание должно быть больше,чем из 2х слов и содержать слова "превосходно, роскошно" ', validators=[catalog.validators.validate_must_be_param], verbose_name='Описание'),
        ),
    ]
