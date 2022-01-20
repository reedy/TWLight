# Generated by Django 3.2.10 on 2021-12-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0080_userprofile_favorites"),
    ]

    operations = [
        migrations.AddField(
            model_name="editor",
            name="wp_block_hash",
            field=models.CharField(
                blank=True,
                editable=False,
                help_text="A hash that is generated with a user's block data",
                max_length=255,
            ),
        ),
    ]
