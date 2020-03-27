# Generated by Django 2.2.11 on 2020-03-15 15:38

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_contentpage_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, default='', help_text='Optional short text description, max. 400 characters', max_length=400),
        ),
    ]