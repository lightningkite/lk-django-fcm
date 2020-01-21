from django.contrib import admin

from .models import FCMDeviceToken


class DeviceTokenAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_display = ('token', 'user', 'active', 'platform',
                    'app_version', 'created_at', 'updated_at',)
    search_fields = ['platform', 'app_version', ]
    actions = ['send_test_notification']
    list_filter = ('platform', 'app_version', 'active',)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.method == 'GET'

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return super(DeviceTokenAdmin, self).save_model(
                request, obj, form, change)

    def delete_model(self, request, obj):
        if request.user.is_superuser:
            return super(DeviceTokenAdmin, self).save_model(request, obj)

    def save_related(self, request, form, formsets, change):
        if request.user.is_superuser:
            return super(DeviceTokenAdmin, self).save_related(
                request, form, formsets, change)

    def get_actions(self, request):
        actions = super(DeviceTokenAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['token', 'platform', 'app_version', 'user', 'active']
        return []

    def send_test_notification(self, request, queryset):
        body = FCMDeviceToken.construct_body(
            'Test notification', 'test', 'This is a test notification', None)
        for token in queryset:
            token.send_notification(body)
    send_test_notification.short_description = "Send test notification"
