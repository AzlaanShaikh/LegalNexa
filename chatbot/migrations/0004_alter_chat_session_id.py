# Generated by Django 5.0.3 on 2024-03-25 10:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatbot", "0003_alter_chat_session_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="session_id",
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
