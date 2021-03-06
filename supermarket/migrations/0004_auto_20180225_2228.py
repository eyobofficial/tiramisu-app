# Generated by Django 2.0.2 on 2018-02-25 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0003_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Floor Section Title')),
                ('floor', models.CharField(choices=[('first', 'First Floor'), ('second', 'Second Floor'), ('third', 'Third Floor')], max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['floor', 'title'],
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supermarket.Section'),
        ),
    ]
