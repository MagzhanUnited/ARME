# Generated by Django 4.1.5 on 2023-02-02 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_product_city_product_isdeliver_product_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cartype',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True,on_delete=django.db.models.deletion.CASCADE, to='apps.person'),
            preserve_default=False,
        ),
    ]
