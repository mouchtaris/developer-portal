# Generated by Django 2.2.11 on 2020-03-23 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0049_topic_nav_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='latest_articles_count',
        ),
    ]