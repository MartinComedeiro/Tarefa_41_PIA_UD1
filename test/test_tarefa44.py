from tarefa41.tarefa44 import resta,ejecutarLista

lista = [0, 3, 2, 4, 6, 3, 4]

def test_resta_correcta():
    assert resta(5) == 3

def test_ejecutar_lista_correcta():
    assert ejecutarLista(lista, resta) == [-2, 1, 0, 2, 4, 1, 2]

