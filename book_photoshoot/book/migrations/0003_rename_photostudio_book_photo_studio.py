# Generated by Django 5.0.3 on 2024-03-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='photostudio',
            new_name='photo_studio',
        ),
    ]
