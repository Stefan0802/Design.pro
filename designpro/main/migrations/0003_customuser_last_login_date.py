# Generated by Django 5.1.3 on 2024-11-11 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_login_count_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_login_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]