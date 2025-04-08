from django.contrib import admin
from .models import RendezVous
from django.utils.html import format_html

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'avocat', 'date', 'statut')
    list_filter = ('statut', 'date', 'avocat')
    search_fields = ('client__user__first_name', 'avocat__user__last_name', 'motif')
    ordering = ('-date',)
    date_hierarchy = 'date'
    actions = ['marquer_annule']
    readonly_fields = ('duree_rdv',)

    #Permettre à l'admin de marquer plusieurs RDV comme "Annulés" d'un coup
    def marquer_annule(self, request, queryset):
        queryset.update(statut='A')
    marquer_annule.short_description = "Marquer comme annulé"

    #Afficher la durée restante avant le RDV
    def dans_combien_de_jours(self, obj):
        from django.utils import timezone
        delta = obj.date - timezone.now()
        return f"{delta.days} jours"
    dans_combien_de_jours.short_description = "Jours restants"

    #pour afficher des données calculées en couleur directement dans l'admin
    def duree_rdv(self, obj):
        return format_html('<span style="color: {};">{} min</span>', 'green', 30)
    duree_rdv.short_description = "Durée estimée"


