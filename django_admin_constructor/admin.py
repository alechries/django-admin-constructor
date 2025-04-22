from django.contrib import admin
from .models import ModelFactory

def create_dynamic_admin(model_class):
  
    class DynamicModelAdmin(admin.ModelAdmin):

        list_display = [field.name for field in model_class._meta.get_fields()]
      
        fields = [field.name for field in model_class._meta.get_fields()]
      
        search_fields = [field.name for field in model_class._meta.get_fields() if isinstance(field, models.CharField)]

    return DynamicModelAdmin


# product_model = ModelFactory.get_model('Product')
# dynamic_admin_class = create_dynamic_admin(product_model)
# admin.site.register(product_model, dynamic_admin_class)
