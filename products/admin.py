from django.contrib import admin

# Register your models here.
import products.models


admin.site.register(products.models.Product)
admin.site.register(products.models.ProductStore)
admin.site.register(products.models.Category)
admin.site.register(products.models.Store)
admin.site.register(products.models.CategryFeature)
admin.site.register(products.models.Color)
admin.site.register(products.models.Warranty)


