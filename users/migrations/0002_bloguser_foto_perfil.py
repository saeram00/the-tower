# Generated by Django 4.0.4 on 2022-05-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='foto_perfil',
            field=models.ImageField(default='default.jpg', upload_to='profile-pics'),
        ),
    ]