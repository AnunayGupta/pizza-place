# Generated by Django 3.0.4 on 2020-03-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200329_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatter',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='style',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.CharField(choices=[('Cheese', 'Cheese'), ('1 Topping', '1 Topping'), ('2 Toppings', '2 Toppings'), ('3 Toppings', '3 Toppings'), ('Special', 'Special')], default='CH', max_length=15),
        ),
        migrations.AlterField(
            model_name='pizza_order',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza_order',
            name='style',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza_order',
            name='type',
            field=models.CharField(choices=[('Cheese', 'Cheese'), ('1 Topping', '1 Topping'), ('2 Toppings', '2 Toppings'), ('3 Toppings', '3 Toppings'), ('Special', 'Special')], default='0', max_length=15),
        ),
        migrations.AlterField(
            model_name='sub',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], max_length=10),
        ),
    ]
