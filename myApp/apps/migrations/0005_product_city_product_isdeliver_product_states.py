# Generated by Django 4.1.5 on 2023-02-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='isDeliver',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='states',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]