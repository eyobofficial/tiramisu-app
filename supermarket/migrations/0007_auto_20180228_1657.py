# Generated by Django 2.0.2 on 2018-02-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0006_catagory_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='catagory/thumbnails/'),
        ),
    ]