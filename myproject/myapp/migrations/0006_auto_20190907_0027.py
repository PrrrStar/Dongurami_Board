# Generated by Django 2.1.5 on 2019-09-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190907_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_db',
            name='c_writer',
            field=models.CharField(max_length=10),
        ),
    ]
