from tarefa41.tarefa43 import IVE,IVE4,descuento,ejecutarLista

lista = [
    {
    "produto": "Pan",
    "prezo_sen_ive": 1.20,
    "desconto": None, # Non ten desconto
    "calcular_ive": IVE4
    },
    {
    "produto": "Aceite de oliva",
    "prezo_sen_ive": 8.50,
    "desconto": descuento, # Aplica un 10%
    "calcular_ive": IVE
    },
    {
    "produto": "Deterxente",
    "prezo_sen_ive": 6.00,
    "desconto": descuento,
    "calcular_ive": IVE
    },
    {
    "produto": "Leite",
    "prezo_sen_ive": 0.95,
    "desconto": None,
    "calcular_ive": IVE4
    }
]

def test_IVE_correcta():
    assert IVE(100) == 79

def test_IVE4_correcta():
    assert IVE4(100) == 96

def test_descuento_correcto():
    assert descuento(100) == 90

def test_ejecutar_lista_correcta():
    assert ejecutarLista(lista) == [16.65, 12.3735, 1.4499999999999993, 2.8264999999999993]

