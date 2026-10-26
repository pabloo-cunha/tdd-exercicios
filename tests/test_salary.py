import pytest

from salary import CalculadoraSalario, Cargo, Funcionario


def _funcionario(salario_base: float, cargo: Cargo) -> Funcionario:
    return Funcionario("Fulano Silva", "fulano@empresa.com", salario_base, cargo)


def test_desenvolvedor_salario_abaixo_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(2999.99, Cargo.DESENVOLVEDOR)
    )
    assert liquido == pytest.approx(2699.991)


def test_desenvolvedor_salario_igual_ao_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(3000, Cargo.DESENVOLVEDOR)
    )
    assert liquido == pytest.approx(2400)


def test_desenvolvedor_salario_acima_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(4000, Cargo.DESENVOLVEDOR)
    )
    assert liquido == pytest.approx(3200)


def test_dba_salario_abaixo_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(1999.99, Cargo.DBA)
    )
    assert liquido == pytest.approx(1699.9915)


def test_dba_salario_igual_ao_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(2000, Cargo.DBA)
    )
    assert liquido == pytest.approx(1500)


def test_testador_salario_abaixo_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(1500, Cargo.TESTADOR)
    )
    assert liquido == pytest.approx(1275)


def test_testador_salario_acima_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(2500, Cargo.TESTADOR)
    )
    assert liquido == pytest.approx(1875)


def test_gerente_salario_abaixo_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(4999.99, Cargo.GERENTE)
    )
    assert liquido == pytest.approx(3999.992)


def test_gerente_salario_igual_ao_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(5000, Cargo.GERENTE)
    )
    assert liquido == pytest.approx(3500)


def test_gerente_salario_acima_do_limiar():
    liquido = CalculadoraSalario().calcula_salario_liquido(
        _funcionario(6000, Cargo.GERENTE)
    )
    assert liquido == pytest.approx(4200)
