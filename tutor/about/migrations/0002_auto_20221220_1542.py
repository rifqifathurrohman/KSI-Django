# Generated by Django 3.1 on 2022-12-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='alamat',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='nama',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
    ]
