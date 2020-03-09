# Generated by Django 2.2.6 on 2020-03-09 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200112_1512'),
        ('menu', '0002_auto_20200115_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='is_category',
        ),
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='articles.Category'),
            preserve_default=False,
        ),
    ]