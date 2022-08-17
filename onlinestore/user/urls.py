from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('<slug:product_name>', view.product),
    path('profile/<slug:profile>', view.user_profile),
]



