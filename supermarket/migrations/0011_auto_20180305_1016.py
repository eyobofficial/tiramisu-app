# Generated by Django 2.0.2 on 2018-03-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0010_auto_20180305_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-featured', 'title'], 'verbose_name': 'Product Brand', 'verbose_name_plural': 'Product Brands'},
        ),
    ]