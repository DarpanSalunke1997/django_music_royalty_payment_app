# Generated by Django 3.2.6 on 2021-08-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210826_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='RBT_MAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ARTIST_NAME', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('CONTENT_NAME', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('REV_X_2', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]