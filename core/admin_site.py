from django.contrib.admin import AdminSite
from django.contrib.admin.views import redirect_to_login
from django.urls import reverse

class CustomAdminSite(AdminSite):
    def has_permission(self, request):
        if request.user.is_active and request.user.is_staff and request.user.is_superuser:
            return True
        return False

    def login(self, request, extra_context=None):
        if not request.user.is_authenticated or not self.has_permission(request):
            return redirect_to_login(
                reverse('admin:login'),
                reverse('admin:logout'),
                self.login_url,
                self.redirect_field_name
            )
        return super().login(request, extra_context)

admin_site = CustomAdminSite(name='custom_admin')
