# Generated by Django 2.2 on 2021-09-24 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenseitem',
            old_name='expenses',
            new_name='expense',
        ),
        migrations.RemoveField(
            model_name='expenseitem',
            name='goal_amount',
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='loginRegApp.User'),
        ),
    ]
