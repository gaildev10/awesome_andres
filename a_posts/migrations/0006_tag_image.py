# Generated by Django 5.1.1 on 2024-09-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0005_alter_tag_options_tag_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
