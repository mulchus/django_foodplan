# Generated by Django 4.2.5 on 2023-09-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(default=0, verbose_name='калорий'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='meal_time',
            field=models.CharField(choices=[('Завтрак', 'Завтрак'), ('Обед', 'Обед'), ('Ужин', 'Ужин'), ('Десерт', 'Десерт')], max_length=10, verbose_name='время приема пищи'),
        ),
    ]
