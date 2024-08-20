from django.contrib import admin
# Add Feeding to the import
from .models import Cat, Feeding, Toy

admin.site.register(Cat)
# Register the new Feeding model
admin.site.register(Feeding)
# Add the Toy model
admin.site.register(Toy)