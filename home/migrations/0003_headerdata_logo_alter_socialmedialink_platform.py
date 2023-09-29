# Generated by Django 4.2.5 on 2023-09-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_headerdata_social_media_account_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerdata',
            name='logo',
            field=models.CharField(default='Villa', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='platform',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('LinkedIn', 'LinkedIn'), ('Instagram', 'Instagram')], max_length=50),
        ),
    ]