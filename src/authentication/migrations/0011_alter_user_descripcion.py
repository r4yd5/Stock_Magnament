# Generated by Django 4.0.6 on 2022-08-28 02:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_user_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
