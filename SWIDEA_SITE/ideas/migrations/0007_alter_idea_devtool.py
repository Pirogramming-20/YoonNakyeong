# Generated by Django 5.0.1 on 2024-01-17 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_alter_idea_devtool'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.tool', verbose_name='예상 개발툴'),
        ),
    ]