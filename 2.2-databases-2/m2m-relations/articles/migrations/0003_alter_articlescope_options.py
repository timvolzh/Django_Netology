# Generated by Django 4.0.4 on 2022-04-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlescope_alter_article_options_alter_article_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['-is_main', 'tag'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]