# Generated by Django 4.0.6 on 2023-01-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendgood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.friend', verbose_name='フォローした人')),
                ('goodanime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.anime', verbose_name='アニメ')),
            ],
        ),
    ]
