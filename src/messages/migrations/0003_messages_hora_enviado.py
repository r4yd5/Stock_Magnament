# Generated by Django 4.0.6 on 2022-08-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_remove_messages_hora_enviado'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='hora_enviado',
            field=models.CharField(default='', max_length=20),
        ),
    ]
