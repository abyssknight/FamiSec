from members.models import Member, Badge, BadgeLog
from django.contrib import admin

class BadgeInline(admin.StackedInline):
  model = Badge
  extra = 0
  readonly_fields = ['card_id']

class MemberAdmin(admin.ModelAdmin):
  list_display = ('name', 'alias', 'email_address', 'last_modified')
  inlines = [
      BadgeInline,
  ]

class BadgeAdmin(admin.ModelAdmin):
  list_display = ('card_id', 'owner', 'last_modified')

class BadgeLogAdmin(admin.ModelAdmin):
  list_display = ('card', 'owner', 'login_date')

admin.site.register(Member, MemberAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(BadgeLog, BadgeLogAdmin)
