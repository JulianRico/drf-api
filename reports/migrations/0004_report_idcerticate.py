# Generated by Django 4.2 on 2024-03-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_rename_create_at_report_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='idcerticate',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
