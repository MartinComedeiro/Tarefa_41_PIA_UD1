from tarefa41.tarefa41 import suma

def test_suma_correcta():
    assert suma(5) == 15

def test_suma_negativa_correcta():
    assert suma(-5) == 15

