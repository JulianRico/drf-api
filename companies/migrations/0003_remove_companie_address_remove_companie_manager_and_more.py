# Generated by Django 4.2 on 2023-08-01 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_companie_usercompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companie',
            name='address',
        ),
        migrations.RemoveField(
            model_name='companie',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='companie',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='companie',
            name='userCompany',
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('emailContact', models.EmailField(max_length=254)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('companie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Company', to='companies.companie')),
            ],
        ),
    ]
