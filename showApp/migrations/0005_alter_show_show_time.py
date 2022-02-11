# Generated by Django 4.0 on 2022-02-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showApp', '0004_alter_show_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_time',
            field=models.TimeField(choices=[(10, 'Morning show'), (14, 'Afternoon show'), (18, 'Evening show'), (22, 'Night show')]),
        ),
    ]