# Generated by Django 4.0.3 on 2022-03-25 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_scope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-tag'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
