from enum import Enum


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: float, cargo: Cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:
    _REGRAS = {
        Cargo.DESENVOLVEDOR: (3000.0, 0.20, 0.10),
        Cargo.DBA: (2000.0, 0.25, 0.15),
        Cargo.TESTADOR: (2000.0, 0.25, 0.15),
        Cargo.GERENTE: (5000.0, 0.30, 0.20),
    }

    def calcula_salario_liquido(self, funcionario: Funcionario) -> float:
        limiar, desconto_alto, desconto_baixo = self._REGRAS[funcionario.cargo]
        desconto = (
            desconto_alto
            if funcionario.salario_base >= limiar
            else desconto_baixo
        )
        return funcionario.salario_base * (1 - desconto)
