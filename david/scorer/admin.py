from django.contrib import admin
# Register your models here.
from .models import DiscreteMath, DataCommunication, ComputerOrganisationArchitecture, SoftwareEngineering, ProbabilityAndStatistics, DataStructures

admin.site.site_header = "Scorer Admin"
admin.site.site_title = "Scorer Admin Portal"
admin.site.index_title = "Welcome to The Scorer Admin"

admin.site.register(DiscreteMath)
admin.site.register(ComputerOrganisationArchitecture)
admin.site.register(DataCommunication)
admin.site.register(SoftwareEngineering)
admin.site.register(ProbabilityAndStatistics)
admin.site.register(DataStructures)
