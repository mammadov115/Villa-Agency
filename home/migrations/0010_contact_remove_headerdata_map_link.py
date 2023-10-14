# Generated by Django 4.2.6 on 2023-10-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_headerdata_map_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=250)),
                ('map_link', models.TextField(help_text='Enter Google Map location embed code')),
            ],
        ),
        migrations.RemoveField(
            model_name='headerdata',
            name='map_link',
        ),
    ]