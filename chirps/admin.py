from django.contrib import admin
from .models import *


# Register your models here.

class ChirpLikeAdmin(admin.TabularInline):
    model = ChirpLike

class ChirpAdmin(admin.ModelAdmin):
    inlines = [ChirpLikeAdmin]
    list_display = ["id", "content", "user"]
    search_fields = ["content", "user__username", "user__email"]
    class Meta:
        model = Chirp
        

admin.site.register(Chirp, ChirpAdmin)

# admin.site.register(User)

