from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario'  # Asegúrate de que name sea 'inventario' y no 'inventory'
    verbose_name = 'Inventario'  # Cambia el nombre que se muestra en el panel de administración

