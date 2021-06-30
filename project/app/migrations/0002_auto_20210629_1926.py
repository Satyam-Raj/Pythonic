# Generated by Django 3.2.4 on 2021-06-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.BooleanField(choices=[('1', 'Male'), ('2', 'Female')])),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]