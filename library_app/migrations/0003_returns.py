# Generated by Django 5.1.3 on 2024-11-30 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField()),
                ('Book', models.ManyToManyField(to='library_app.book')),
                ('Reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.reader')),
            ],
        ),
    ]