import unittest
from suma import suma
from resta import resta
from producto import producto
from cociente import cociente
from potencia import potencia
from radicacion import radicacion
from modulo import modulo
from a11g2 import *


class TestStringMethods(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(1,6),1+6)
        self.assertEqual(suma(15.4,-15),15.4+-15)
        self.assertEqual(suma(999,-998),1)
        self.assertEqual(suma(-25.78,-25.72),-51.5)
    
    def test_resta(self):
        self.assertEqual(resta(1,6),-5)
        self.assertEqual(resta(15,-15),30)
        self.assertEqual(resta(999,-998),1997)
        self.assertEqual(resta(-25.78,-25.72),-0.060000000000002274)
    
    def test_producto(self):
        self.assertEqual(producto(1,6),6)
        self.assertEqual(producto(15,-15),-225)
        self.assertEqual(producto(999,-998),-997002)
        self.assertEqual(producto(-25.78,-25.72),663.0616)
    
    def test_cociente(self):
        self.assertEqual(cociente(10,10),1)
        self.assertEqual(cociente(100,10),10)
        self.assertEqual(cociente(1,0),'No se puede dividir por cero')
    
    def test_potencia(self):
        self.assertEqual(potencia(2,2),4)
        self.assertEqual(potencia(2,-2),0.25)
        self.assertEqual(potencia(2,0),1)
    
    def test_radicacion(self):
        self.assertEqual(radicacion(2,2),1.414)
        self.assertEqual(radicacion(2,-2),0.707)
        self.assertEqual(radicacion(1,0),'No se puede dividir por cero')
    
    def test_modulo(self):
        self.assertEqual(modulo(2,2),0)
        self.assertEqual(modulo(77,-2),-1)
        self.assertEqual(modulo(1550,0),'No se puede dividir por cero')
    
    def test_p1(self):
        self.assertEqual(p1(1,2,3),5)
        self.assertEqual(p1(2,-2,3),-1)
        self.assertEqual(p1(84,-77,8),-6460)
    
    def test_p2(self):
        self.assertEqual(p2(84,-77,8),(84+-77)*8)
        self.assertEqual(p2(1950,72.5,3),(1950+72.5)*3)

    def test_p3(self):
        self.assertEqual(p3(84,-77,8),(84--77)*8)
        self.assertEqual(p3(1950,72.5,3),(1950-72.5)*3)

    def test_genrnd(self):
        self.assertEqual(len(genrnd()),50)

    def test_suma_lista(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(suma_lista(_aux),-1703)

    def test_cociente_lista(self):
        self.assertEqual(len(cociente_lista(genrnd())),50)
    
    def test_calcula_media(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_media(_aux),-34.06)
    
    def test_calcula_mediana(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_mediana(_aux),-851.5)
    
    def test_calcula_rango(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_rango(_aux),[-255,256])
    
    def test_calcula_varianza(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_varianza(_aux),139.672)

    def test_calcula_min(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_min(_aux),-255)
    
    def test_calcula_min(self):
        _aux=[-63, -242, -255, 143, 128, 72, -13, -111, -57, 178, 36, -79, 75, -213, 160, -61, 5, -255, -228, -6, -112, -211, 58, -215, 22, -62, 59, -237, -32, -150, -65, -222, 256, -77, -190, -200, -23, -206, 112, -103, -145, 100, 101, 17, 151, -83, 176, 125, 163, 76]
        self.assertEqual(calcula_max(_aux),256)

    def test_genrnd5e(self):
        self.assertEqual(len(genrnd5e()),50000)
        




    
        
    
    
        



        
    

    
    
  


if __name__ == '__main__':
    unittest.main()