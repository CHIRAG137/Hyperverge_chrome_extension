# Generated by Django 5.0.7 on 2024-07-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='content',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
