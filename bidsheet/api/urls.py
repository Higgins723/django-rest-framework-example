from django.conf.urls import url
from .views import (
    BidSheetAPIView,
    BidSheetAPIDetailView,
)


urlpatterns = [
    url(r'^$', BidSheetAPIView.as_view(), name="list"),
    url(r'^(?P<id>\d+)/$', BidSheetAPIDetailView.as_view(), name="detail"),
]