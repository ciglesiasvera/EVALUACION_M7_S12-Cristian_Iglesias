from django.test import TestCase
from .models import Producto, Fabrica
from django.urls import reverse

#Ejercicio 1.-
""" class FabricaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Fabrica.objects.create(nombre='Fabrica Test', pais='Test Location')

    def test_model_content_fabrica(self):
        fabrica = Fabrica.objects.get(id=1)
        expected_nombre = 'Fabrica Test'
        expected_pais = 'Test Location'
        self.assertEqual(fabrica.nombre, expected_nombre)
        self.assertEqual(fabrica.pais, expected_pais) """

#Ejercicio 2.-        
""" class ProductoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        fabrica = Fabrica.objects.create(nombre='Fabrica Test', pais='Test Location')
        Producto.objects.create(
            nombre='Producto Test',
            descripcion='Test Description',
            precio=100.00,
            f_vencimiento='2023-12-31',
            fabrica=fabrica
        )

    def test_model_content_producto(self):
        producto = Producto.objects.get(id=1)
        expected_nombre = 'Producto Test'
        expected_descripcion = 'Test Description'
        expected_precio = 100.00
        expected_f_vencimiento = '2023-12-31'
        expected_fabrica_nombre = 'Fabrica Test'
        
        self.assertEqual(producto.nombre, expected_nombre)
        self.assertEqual(producto.descripcion, expected_descripcion)
        self.assertEqual(producto.precio, expected_precio)
        self.assertEqual(str(producto.f_vencimiento), expected_f_vencimiento)
        self.assertEqual(producto.fabrica.nombre, expected_fabrica_nombre) """

#Ejercicio 3.- 
""" class RegistrarProductoViewTest(TestCase):

    def test_registrar_url(self):
        response = self.client.get(reverse('registrar_producto'))
        self.assertEqual(response.status_code, 200) """
        
#Ejercicio 4.-
class ProductoListViewTest(TestCase):

    def test_producto_list_url(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/producto_list.html')
        self.assertContains(response, 'Información de Productos')
