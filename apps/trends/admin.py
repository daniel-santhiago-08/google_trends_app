from django.contrib import admin
from .models import TrendsRising


class TrendsRisingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return TrendsRising.objects.using('google_trends_crawler').all()


admin.site.register(TrendsRising, TrendsRisingAdmin)
