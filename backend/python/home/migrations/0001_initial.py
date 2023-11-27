# Generated by Django 4.2.7 on 2023-11-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Files',
                'ordering': ['date_uploaded'],
            },
        ),
    ]