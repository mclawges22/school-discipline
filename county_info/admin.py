from django.contrib import admin
from county_info.models import District, Graduation

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('lea_name', 'lea_code', 'lea_city', 'lea_state', 'lea_superintendent', 'lea_email', 'lea_website')
	search_fields = ('lea_name', 'lea_city')

admin.site.register(District, DistrictAdmin)

class GraduationAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'graduation_rate', 'female_graduation_rate', 'male_graduation_rate', 'freelunch_graduation_rate', 'black_graduation_rate', 'hispanic_graduation_rate')
	search_fields = ('code',)

admin.site.register(Graduation, GraduationAdmin)
