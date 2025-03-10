# Generated by Django 5.0.3 on 2024-04-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='home')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
