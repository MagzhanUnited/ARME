# Generated by Django 4.1.5 on 2023-01-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fullname',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
