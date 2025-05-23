# Generated by Django 5.1.7 on 2025-04-05 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at'], 'verbose_name': 'WhatsApp Message', 'verbose_name_plural': 'WhatsApp Messages'},
        ),
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'ordering': ['-created_at'], 'verbose_name': 'WhatsApp Phone Number', 'verbose_name_plural': 'WhatsApp Phone Numbers'},
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='api_verified',
            field=models.BooleanField(default=False, help_text="Check when you've verified the API connection", verbose_name='API Connection Verified'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='test_message_sent',
            field=models.BooleanField(default=False, help_text="Check when you've successfully sent a test message", verbose_name='Test Message Sent'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='webhook_configured',
            field=models.BooleanField(default=False, help_text="Check when you've configured the webhook in Meta Developer Portal", verbose_name='Webhook Configured'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='message',
            name='direction',
            field=models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], default='inbound', max_length=10, verbose_name='Direction'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_number',
            field=models.CharField(max_length=20, verbose_name='From Number'),
        ),
        migrations.AlterField(
            model_name='message',
            name='media_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Media ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='media_url',
            field=models.URLField(blank=True, null=True, verbose_name='Media URL'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Message ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_type',
            field=models.CharField(default='text', max_length=50, verbose_name='Message Type'),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='whatsapp.phonenumber', verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('delivered', 'Delivered'), ('read', 'Read'), ('failed', 'Failed')], default='sent', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_number',
            field=models.CharField(max_length=20, verbose_name='To Number'),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='business_account_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Business Account ID'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='display_name',
            field=models.CharField(max_length=100, verbose_name='Display Name'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Phone Number ID'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]
