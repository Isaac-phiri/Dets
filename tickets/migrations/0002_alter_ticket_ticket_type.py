# Generated by Django 5.0.4 on 2024-05-04 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('General Admission', 'General Admission'), ('VIP', 'VIP'), ('Student', 'Student'), ('Senior Citizen', 'Senior Citizen'), ('Child', 'Child'), ('Senior', 'Senior')], max_length=100),
        ),
    ]
