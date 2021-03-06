# Generated by Django 3.2.6 on 2021-08-26 06:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kineto_Kisom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('content_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('net_royalty_total', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('Editor', 'Editor'), ('Artist', 'Artist'), ('Admin', 'Admin')], max_length=50, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '123456789' ", regex='^[0-9]+$')])),
                ('type', models.CharField(blank=True, choices=[('Grupo', 'Grupo'), ('Solo', 'Solo')], max_length=50, null=True)),
                ('file_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('account_holder_nm', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('IBAN', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
