from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    icon=models.TextField(blank=True)
    hide=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Products(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    site_product_id=models.CharField(max_length=1000,blank=True,null=True)
    title=models.CharField(max_length=1000,blank=True,null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    seller = models.CharField(max_length=255, blank=True, null=True)
    ful_fillment = models.CharField(max_length=255, blank=True, null=True)
    size_tier = models.CharField(max_length=255, blank=True, null=True)
    number_of_images = models.BigIntegerField(default=0,blank=True,null=True)
    variation_count = models.BigIntegerField(default=0,blank=True,null=True)
    weight= models.CharField(max_length=255, blank=True, null=True)
    package_dimensions=models.CharField(max_length=500, blank=True, null=True)
    storage_fee =models.CharField(max_length=500, blank=True, null=True)
    Age_month=models.BigIntegerField(default=0,blank=True,null=True)
    sellers = models.BigIntegerField(default=0,blank=True,null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    monthly_sales = models.CharField(max_length=255, blank=True, null=True)
    monthly_revenue=models.CharField(max_length=255, blank=True, null=True)
    bsr=models.CharField(max_length=255, blank=True, null=True)
    reviwes=models.CharField(max_length=255, blank=True, null=True)
    last_year_sales:models.CharField(max_length=255, blank=True, null=True)
    sales_year_over_year=models.CharField(max_length=255, blank=True, null=True)
    sales_trend=models.CharField(max_length=255, blank=True, null=True)
    price_trend=models.CharField(max_length=255, blank=True, null=True)
    best_sales_period=models.CharField(max_length=255, blank=True, null=True)
    sales_to_reviews=models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)