# Generated by Django 4.2.4 on 2023-08-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название_города')),
            ],
            options={
                'verbose_name': 'Название_города',
                'verbose_name_plural': 'Название_городов',
                'ordering': ['name'],
            },
        ),
    ]