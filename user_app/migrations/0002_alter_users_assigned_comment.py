# Generated by Django 4.2.4 on 2024-01-04 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments_task', '0002_initial'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='assigned_comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='comments_task.comments'),
        ),
    ]