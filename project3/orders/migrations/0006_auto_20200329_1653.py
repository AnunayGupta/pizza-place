# Generated by Django 3.0.4 on 2020-03-29 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_auto_20200329_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'Cheese'), ('1', '1 Topping'), ('2', '2 Toppings'), ('3', '3 Toppings'), ('5', 'Special')], default='0', max_length=15)),
                ('style', models.CharField(choices=[('R', 'Regular'), ('S', 'Sicilian')], max_length=10)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
                ('quantity', models.IntegerField(default=1)),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]