# Generated by Django 4.2.3 on 2024-02-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_article_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="title",
            field=models.CharField(default="What is lorem ipsum ? ", max_length=255),
            preserve_default=False,
        ),
    ]
