# Generated by Django 2.2 on 2021-09-24 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
