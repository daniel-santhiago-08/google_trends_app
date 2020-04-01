from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    TrendsRisingList
)



urlpatterns = [
    path('ascencao/', TrendsRisingList.as_view(), name='list_trends_rising' ),
    path('ascencao-csv', TrendsRisingList.export_csv, name='csv_rising'),
    # path('min/', PriceCrawlerMinList.as_view(), name='list_price_crawler_min' ),
    # path('min-export-csv/', PriceCrawlerMinList.export_csv, name='csv_min' ),
    # path('evolution/', PriceCrawlerEvolutionList.as_view(), name='list_price_crawler_evolution' ),
    # path('evolution-export-csv/', PriceCrawlerEvolutionList.export_csv, name='csv_evolution'),
    # path('line-chart/', PriceCrawlerLineChart.as_view(), name='price_crawler_line'),
    # path('prints/', PriceCrawlerPrintList.as_view(), name='list_price_crawler_prints' ),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)