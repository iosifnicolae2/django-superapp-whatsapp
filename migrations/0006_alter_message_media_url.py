# Generated by Django 5.1.8 on 2025-04-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0005_contact_phonenumber_api_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='media_url',
            field=models.ImageField(blank=True, null=True, upload_to='whatsapp_media/', verbose_name='media URL'),
        ),
    ]
