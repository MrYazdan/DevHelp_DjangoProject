from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing/shop.html"), name="home"),
    path('', include("settings.urls")),
    path('admin/', admin.site.urls),
    path('account/', include("account.urls"), name="account"),
    path('core/', include("core.urls"), name="core"),
    path('cart/', include("order.urls"), name="cart"),
    path('products/', include("products.urls"), name="products"),
    path('category/', include("category.urls"), name="category"),
    path('api/', include("api.urls"), name="api"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
