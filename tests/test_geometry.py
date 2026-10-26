from geometry import Triangle


def test_escaleno_valido():
    assert Triangle(3, 4, 5).classificar() == "escaleno"


def test_isosceles_valido():
    assert Triangle(5, 5, 3).classificar() == "isosceles"


def test_equilatero_valido():
    assert Triangle(5, 5, 5).classificar() == "equilatero"


def test_isosceles_permutacao_aab():
    assert Triangle(5, 5, 3).classificar() == "isosceles"


def test_isosceles_permutacao_aba():
    assert Triangle(5, 3, 5).classificar() == "isosceles"


def test_isosceles_permutacao_baa():
    assert Triangle(3, 5, 5).classificar() == "isosceles"


def test_valor_zero():
    assert Triangle(0, 5, 5).classificar() == "invalido"


def test_valor_negativo():
    assert Triangle(-1, 5, 5).classificar() == "invalido"


def test_soma_igual_terceiro_abc():
    assert Triangle(1, 2, 3).classificar() == "invalido"


def test_soma_igual_terceiro_acb():
    assert Triangle(1, 3, 2).classificar() == "invalido"


def test_soma_igual_terceiro_cab():
    assert Triangle(3, 1, 2).classificar() == "invalido"


def test_soma_menor_terceiro_abc():
    assert Triangle(1, 2, 4).classificar() == "invalido"


def test_soma_menor_terceiro_acb():
    assert Triangle(1, 4, 2).classificar() == "invalido"


def test_soma_menor_terceiro_cab():
    assert Triangle(4, 1, 2).classificar() == "invalido"


def test_tres_valores_zero():
    assert Triangle(0, 0, 0).classificar() == "invalido"
