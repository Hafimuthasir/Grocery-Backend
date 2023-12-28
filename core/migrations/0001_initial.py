# Generated by Django 5.0 on 2023-12-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('produce', 'Produce'), ('dairy', 'Dairy'), ('meat', 'Meat'), ('grains', 'Grains'), ('canned_goods', 'Canned Goods'), ('fruits', 'Fruits')], max_length=50)),
                ('stock', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('kgs', 'Kgs'), ('grams', 'Grams'), ('liters', 'Liters'), ('number', 'Number')], max_length=50)),
            ],
        ),
    ]