# Generated by Django 2.0.2 on 2018-02-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0005_auto_20180226_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='catagory/thumbnails/'),
            preserve_default=False,
        ),
    ]
