# Generated by Django 3.0.8 on 2020-08-18 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOOLS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255)),
                ('site_product_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('seller', models.CharField(blank=True, max_length=255, null=True)),
                ('ful_fillment', models.CharField(blank=True, max_length=255, null=True)),
                ('size_tier', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_images', models.BigIntegerField(blank=True, default=0, null=True)),
                ('variation_count', models.BigIntegerField(blank=True, default=0, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
                ('package_dimensions', models.CharField(blank=True, max_length=500, null=True)),
                ('storage_fee', models.CharField(blank=True, max_length=500, null=True)),
                ('Age_month', models.BigIntegerField(blank=True, default=0, null=True)),
                ('sellers', models.BigIntegerField(blank=True, default=0, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('monthly_sales', models.CharField(blank=True, max_length=255, null=True)),
                ('monthly_revenue', models.CharField(blank=True, max_length=255, null=True)),
                ('bsr', models.CharField(blank=True, max_length=255, null=True)),
                ('reviwes', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_year_over_year', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_trend', models.CharField(blank=True, max_length=255, null=True)),
                ('price_trend', models.CharField(blank=True, max_length=255, null=True)),
                ('best_sales_period', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_to_reviews', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]