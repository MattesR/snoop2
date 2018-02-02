# Generated by Django 2.0 on 2018-01-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_auto_20180126_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name_plural': 'directories'},
        ),
        migrations.AlterModelOptions(
            name='taskdependency',
            options={'verbose_name_plural': 'task dependencies'},
        ),
        migrations.AddField(
            model_name='task',
            name='broken_reason',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
