# Generated by Django 4.1 on 2023-02-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='away_goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='results',
            name='home_goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='results',
            name='round',
            field=models.PositiveIntegerField(default=1),
        ),
    ]