# Generated by Django 2.0 on 2017-12-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]