# Generated by Django 4.1.5 on 2023-01-21 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options_alter_tag_options_tag_articles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]
