from django.db import models
import uuid

# global var for stock status
STOCK_STATUS =  [
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
] 

# product model
class Product(models.Model):
    # product id
    product_id    = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    # product name
    product_name  = models.CharField(max_length=150, null=False, blank=False)
    # product code
    product_code  = models.CharField(max_length=20, null=False, blank=False)
    # factory price
    factory_price = models.CharField(max_length=20, null=False, blank=False)
    # selling peice 
    selling_price = models.CharField(max_length=20, null=False, blank=False)
    # stock status
    stock_status  = models.CharField(max_length=20, null=False, blank=False, choices=STOCK_STATUS)
    # category
    category      = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    # size
    product_size  = models.CharField(max_length=150, blank=False, null=False,)
    # description
    product_des   = models.TextField(blank=True, null=True)
    # create date
    created_at    = models.DateTimeField(auto_now_add=True, editable=False)
    # update
    update_at     = models.DateTimeField(auto_now=True, editable=False)
    # slug
    slug          = models.SlugField(allow_unicode = True, unique=True, blank=True, max_length=255)
    # count views
    views_count   = models.IntegerField(default=0, null=True, blank=True)
        
    def __str__(self) -> str:
        return self.product_name

# multi images model for product 
class ProductImage(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    img_id  = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    images  = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.products.product_name} images'
    
class Category(models.Model):
    cat_id    = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    cat_title = models.CharField(max_length=255, blank=False, null=False)
    cat_img   = models.ImageField(upload_to='images', blank=False)
    slug      = models.SlugField(allow_unicode = True, unique=True, max_length=255)
    
    def __str__(self) -> str:
        return self.cat_title

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    comment    = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self) -> str:
        return self.product.product_name

class ClientViews(models.Model):
    ip_addr = models.CharField(max_length=150, blank=True, null=True)
    views_time = models.IntegerField(default=0, blank=True, null=True)
    device_type = models.CharField(max_length=300, blank=True, null=True)
    view_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.ip_addr
