# Generated by Django 4.0.3 on 2022-03-25 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_rename_theme_scope_tag_remove_article_scopes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
