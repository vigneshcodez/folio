# Generated by Django 5.0.7 on 2024-07-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_myprofile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
