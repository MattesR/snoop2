# Generated by Django 2.0 on 2018-01-18 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_task_traceback'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='blob_arg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='data.Blob'),
        ),
    ]