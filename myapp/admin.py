from django.contrib import admin
from .models import Issue, Agent, Mechanic

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass

@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    pass

# Register your models here.
