# Generated by Django 4.2.5 on 2023-10-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='slider',
            name='country',
            field=models.CharField(default='Azerbaijan', max_length=150),
            preserve_default=False,
        ),
    ]
