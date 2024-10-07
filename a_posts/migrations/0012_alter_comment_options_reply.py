# Generated by Django 5.1.1 on 2024-09-25 20:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0011_alter_comment_parent_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('body', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repliess', to=settings.AUTH_USER_MODEL)),
                ('parent_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='a_posts.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]