# Generated by Django 4.0 on 2022-02-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showApp', '0007_alter_show_show_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='price',
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name='show',
            name='seats',
            field=models.IntegerField(default=1),
        ),
    ]
