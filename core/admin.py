from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Todo

# Register the custom user model with UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register the Todo model
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'due_date', 'user')
    list_filter = ('completed',)
    search_fields = ('title', 'user__username')  # Use double underscores to search related user's username

    def user(self, obj):
        return obj.user.username
    user.short_description = 'User'
