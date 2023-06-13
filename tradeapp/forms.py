from django import forms
from django.forms import ModelForm
from .models import Product,ProductImage,Comment,Category
from multiupload.fields import MultiFileField

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exlude = ['slug']
        
        fields = ['product_name','product_code','factory_price','selling_price','stock_status','category','product_size','product_des',]
        labels = {
                'product_name': 'product name',
                'product_code': 'product code',
                'factory_price': 'factory price',
                'selling_price': 'selling price',
                'stock_status': 'stock status',
                'category': 'category',
                'product_size': 'product size',
                'product_des': 'description',
            }
            
        widgets = {
                'product_des': forms.Textarea(attrs={'placeholder':'type descriptions here...'}),
                'product_size': forms.TextInput(attrs={'placeholder': '記得一定要用空格隔開。。'})
            }
        
        
class ImageForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=7)
    class Meta:
        model = ProductImage
        fields = ['images']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': ''
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'type your comments here...',
                'rows': 3,
                'cols':40,
                'autocomplete': 'off'
            }),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']
        fields = ['cat_title', 'cat_img']
        labels = {
            'cat_title': 'title',
            'cat_img': 'image',
            
        }
        
        
        