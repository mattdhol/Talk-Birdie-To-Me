# Generated by Django 3.1.1 on 2021-04-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0025_auto_20201119_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ('date',)},
        ),
        migrations.AddField(
            model_name='score',
            name='number_of_putts',
            field=models.IntegerField(default=0),
        ),
    ]
