# Generated by Django 3.2.6 on 2021-08-26 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kineto_kisom',
            old_name='artist_name',
            new_name='ARTIST_NAME',
        ),
        migrations.RenameField(
            model_name='kineto_kisom',
            old_name='content_name',
            new_name='CONTENT_NAME',
        ),
        migrations.RenameField(
            model_name='kineto_kisom',
            old_name='net_royalty_total',
            new_name='NET_ROYALTY_TOTAL',
        ),
    ]