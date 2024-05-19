# Generated by Django 5.0.3 on 2024-05-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('Staff', 'Staff')], max_length=20),
        ),
    ]
