from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def admin_statistics_view(request):
    return render(request, 'admin/charts.html', {
        'title': 'Graficos'
    })
    
class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        
        if(request.user.is_superuser):
            app_list += [
                {
                    'name': 'Reportes',
                    'app_label': 'Gráficos',
                    'models': [
                        {
                            'name': 'Gráficos',
                            'object_name': 'Gráficos',
                            'admin_url': '/admin/statistics/',
                            'view_only': False,
                        }
                    ],
                },
            ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        url_patterns = [
            path("statistics/", admin_statistics_view), 
        ]
        return url_patterns + urls