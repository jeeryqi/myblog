# Generated by Django 2.0.7 on 2018-08-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=20, verbose_name='博客类型'),
        ),
    ]
