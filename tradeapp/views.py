from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from .models import Product,Category,ProductImage
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import ProductForm,ImageForm
from .models import ClientViews
from .models import Comment
from .forms import CommentForm
from .forms import CategoryForm
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.paginator import Paginator
import socket


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip

def index(request):
    existing_clients = ClientViews.objects.filter()  # Retrieve all ClientViews objects

    if existing_clients.exists():
        existing_client = existing_clients[0]  # Select the first object
    else:
        existing_client = None

    try:
        c_ip = get_client_ip(request)
        header = request.META.get('HTTP_USER_AGENT')

        if existing_client and (existing_client.ip_addr != c_ip or existing_client.device_type != header):
            new_client = ClientViews.objects.create(ip_addr=c_ip, device_type=header)
            new_client.views_time = existing_client.views_time + 1
            new_client.save()
        elif not existing_client:
            new_client = ClientViews.objects.create(ip_addr=c_ip, device_type=header)
            new_client.views_time = 1
            new_client.save()
        else:
            existing_client.views_time += 1
            existing_client.save()

    except Exception as e:
        # Handle any exceptions that occurred during the data saving process
        return e
        
    # ge all categories
    categories = Category.objects.all()
    
    # for cache
    if cache.get(categories):
        categories = cache.get(categories)
    else:
        if categories:
            categories = categories
            cache.set(categories, categories)
        else:
            categories = categories
            
    context = {
        'categories': categories,
    }
    return render(request, 'index.html', context)

def all_products(request):
    # get products by categories
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    # for cache all products
    if cache.get(products):
        products = cache.get(products)
        page = request.GET.get('page')
        pagginator = Paginator(products, 12)
        products = pagginator.get_page(page)
    else:
        if products:
            products = products
            cache.set(products, products)
            page = request.GET.get('page')
            pagginator = Paginator(products, 12)
            products = pagginator.get_page(page)
        else:
            products = products
            
    # filter by categories
    cat_id = request.GET.get('categories')
    
    if cat_id:
        products = Product.objects.filter(category_id=cat_id)
        # for cache
        if cache.get(products):
            products = cache.get(products)
            page = request.GET.get('page')
            pagginator = Paginator(products, 12)
            products = pagginator.get_page(page)
        else:
            if products:
                products = products
                cache.set(products, products)
                page = request.GET.get('page')
                pagginator = Paginator(products, 12)
                products = pagginator.get_page(page)
            else:
                products = products
        
    context = {
        'products':products,
        'categories':categories,
    }
    
    return render(request, 'allproducts.html', context)

def product_details(request, slug):
    # get product detail page
    products = get_object_or_404(Product, slug=slug)
    comment_form  = CommentForm(request.POST)

    products.views_count = products.views_count + 1
    products.save()
    
    # cache for detials
    if cache.get(slug):
        comment_form  = CommentForm()
        products = cache.get(slug)
    else:
        comment_form  = CommentForm()
        products = get_object_or_404(Product, slug=slug)
        cache.set(slug, products)
        
    # comment_form  = CommentForm(request.POST, instance=products)
    if request.method == "POST":
        
        comment_form  = CommentForm(request.POST)
        
        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            comment.product = products
            comment.save()
            
            # Clear the form for the next comment
            comment_form = CommentForm()
    
    else:
        # If it's a GET request, create an empty comment form
        comment_form = CommentForm()
        
            
   
    comments = Comment.objects.filter(product=products).order_by('-date_created')
        
    context = {
        'products':products,
        'comment_form': comment_form,
        'comments':comments,
    }
    
    return render(request, 'details.html', context)

def about_us(request):
    context = {}
    return render(request, 'about.html', context)

def contact_us(request):
    context = {}
    return render(request, 'contact.html', context)

# dashboard
@login_required
def product_management(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    if not request.user.is_authenticated:
        raise Http404
    
    products = Product.objects.all().order_by('-created_at')
    
    context = {
        'products': products,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_product(request):
    
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    if not request.user.is_authenticated:
        raise Http404
    
    product_form = ProductForm()
    image_form = ImageForm()
    
    if request.method == 'POST':
        
        files = request.FILES.getlist('images')
        
        product_form = ProductForm(request.POST)
        
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.slug = slugify(product.product_name, allow_unicode=True) + slugify(product.product_id)
            product.save()
            
            for file in files:
                ProductImage.objects.create(products=product, images=file)
            return redirect('dashboard')

    context = {
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'addproduct.html', context)

@login_required
def update_product(request, slug):
    
    product = Product.objects.get(slug=slug)
    product_form = ProductForm(instance=product)
    
    if request.method == 'POST':
        
        product_form = ProductForm(request.POST, instance=product)
        
        if product_form.is_valid():
        
            product_form.save()
                
            return redirect('dashboard')

    context = {
        'product_form': product_form,
    }
    
    return render(request, 'update.html', context)

def product_list(request, slug):
    categories = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=categories)
    context  = {
        'categories': categories,
        'products': products,
    }
    
    return render(request, 'productlist.html', context)

# search view
def search(request):
    if request.method == "POST":
        searched = request.POST['searching']
        products = Product.objects.filter(product_name__icontains=searched)
        
        if cache.get(products):
            products = cache.get(products)
        else:
            if products:
                products = products
                cache.set(products, products)
            else:
                products = products
            

        context = {
            'searched': searched,
            'products': products,
        }
        return render(request, 'search.html', context)


@login_required
def add_category(request):
    
    category_form = CategoryForm()
    
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        
        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.slug = slugify(category.cat_title, allow_unicode=True) + slugify(category.cat_id)
            category.save()
            
            return redirect('addproduct')
            
    context = {
        'category_form': category_form
    }
    
    return render(request, 'addcategory.html', context)
