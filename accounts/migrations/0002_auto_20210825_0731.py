# Generated by Django 3.2.6 on 2021-08-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='IBAN',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='account_holder_nm',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bank_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='file_no',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(blank=True, choices=[('Grupo', 'Grupo'), ('Solo', 'Solo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Editor', 'Editor'), ('Artist', 'Artist'), ('Admin', 'Admin')], max_length=50, null=True),
        ),
    ]
