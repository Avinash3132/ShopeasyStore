from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

admin.site.site_header = "ShopEasy Administration"
admin.site.site_title = "ShopEasy Admin"
admin.site.index_title = "Welcome to ShopEasy Admin Panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]

# Useful for local development and simple deployments. For a larger production
# deployment, move uploaded media to object storage/CDN.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
