# Generated by Django 4.0.6 on 2022-08-25 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='hora_enviado',
        ),
    ]