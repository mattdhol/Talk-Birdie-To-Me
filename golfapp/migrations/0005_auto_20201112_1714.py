# Generated by Django 3.1.1 on 2020-11-12 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0004_auto_20201111_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('par', models.IntegerField()),
                ('things_to_remember', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golfapp.course'),
            preserve_default=False,
        ),
    ]
