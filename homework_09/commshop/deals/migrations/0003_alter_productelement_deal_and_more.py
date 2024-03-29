# Generated by Django 4.1.5 on 2023-01-17 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_propertytype_name"),
        ("deals", "0002_alter_deal_date_close"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productelement",
            name="deal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product",
                to="deals.deal",
            ),
        ),
        migrations.AlterField(
            model_name="productelement",
            name="prod_inst",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_element",
                to="products.productinstance",
            ),
        ),
    ]
