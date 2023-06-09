# Generated by Django 4.2 on 2023-04-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('text', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('draft', 'Чечрновик'), ('open', 'Открыта'), ('closed', 'Закрыта')], default='draft', max_length=6)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
