# Generated by Django 5.1.8 on 2025-04-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0025_alter_template_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='template_variables',
            field=models.JSONField(blank=True, default=dict, help_text='Variables used in the template, including body parameters and button parameters', null=True, verbose_name='template variables'),
        ),
    ]
