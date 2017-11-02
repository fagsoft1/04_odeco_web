from django.contrib import admin
from imagekit.admin import AdminThumbnail

from web_soluciones.models import Solucion, ItemSolucion, ItemSolucionImagen, Documento


class DocumentoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'documento',
        'orden',
        'icono',
        'activo'
    ]

    filter_horizontal = ['item_solucion', ]


admin.site.register(Documento, DocumentoAdmin)


class DocumentoInline(admin.TabularInline):
    model = Documento.item_solucion.through
    extra = 0


class SolucionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden', ]

    prepopulated_fields = {"slug": ("nombre",)}

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


admin.site.register(Solucion, SolucionAdmin)


class ItemSolucionImagenInline(admin.TabularInline):
    model = ItemSolucionImagen

    fields = [
        'admin_imagen_thumbnail',
        'descripcion',
        'alt_seo',
        'orden',
        'imagen',
        'marca_agua'
    ]
    admin_imagen_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')
    readonly_fields = ['admin_imagen_thumbnail']

    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class ItemSolucionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'solucion', 'orden', 'categoria', 'categoria_dos', 'activo']
    list_editable = ['nombre', 'orden', 'categoria', 'categoria_dos', 'activo']

    inlines = [ItemSolucionImagenInline, DocumentoInline]

    list_filter = ['solucion', 'categoria', 'categoria_dos', 'activo']


admin.site.register(ItemSolucion, ItemSolucionAdmin)
