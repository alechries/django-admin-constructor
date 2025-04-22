from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class ModelFactory:
    _instances = {}

    @staticmethod
    def get_model(name: str):
        """
        Factory-Methode zum Erhalten von Modellen basierend auf dem Namen.
        Es wird nur eine Instanz jedes Modells erstellt.
        """
        if name not in ModelFactory._instances:
            ModelFactory._instances[name] = ModelFactory._create_model(name)
        return ModelFactory._instances[name]

    @staticmethod
    def _create_model(name: str):
        """
        Dynamisches Erstellen eines Modells zur Laufzeit.
        Hier kannst du weitere Feldtypen dynamisch hinzufügen.
        """
        # Die Felder, die das dynamische Modell haben soll.
        fields = {
            'name': models.CharField(max_length=100),
            'price': models.DecimalField(max_digits=10, decimal_places=2),
            'description': models.TextField(),
        }

        # Dynamisch eine Model-Klasse erstellen
        new_model_class = type(name, (models.Model,), fields)
        return new_model_class


# Beispiel für die Verwendung:
product_model = ModelFactory.get_model('Product')

# Jetzt kannst du mit dem dynamischen Modell arbeiten:
product = product_model.objects.create(name="Test Produkt", price=19.99, description="Testbeschreibung")

print(product.name)  # Ausgabe: Test Produkt
