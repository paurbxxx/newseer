# Generated by Django 3.1.5 on 2021-07-02 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('bio', models.CharField(max_length=250)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
    ]
