from tarefa41.tarefa42 import areaCir,volCil

from math import pi

def test_area_circulo_correcto():
    assert areaCir(5) == 25*pi

def test_volumen_cilindro():
    assert volCil(5, 5) == (25*pi)*5

