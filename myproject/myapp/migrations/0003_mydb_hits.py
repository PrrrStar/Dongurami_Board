# Generated by Django 2.1.5 on 2019-09-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190904_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydb',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]