# Exercícios TDD

Projeto com exercícios de TDD em Python (pytest + pytest-cov).

## Estrutura

```
TDD/
├── geometry.py          # Exercício 1
├── person.py            # Exercício 2
├── salary.py            # Exercício 3
├── tests/
│   ├── test_geometry.py
│   ├── test_person.py
│   └── test_salary.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Build

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução dos testes

```bash
pytest -v
```

## Cobertura de código

```bash
pytest --cov=geometry --cov=person --cov=salary --cov-report=term-missing
```

---

# Exercício 1 — Triângulo (TDD)

Classifica três valores inteiros (lados) como triângulo **equilátero**, **isósceles**, **escaleno** ou **inválido**.

Condição de validade: a soma de dois lados deve ser **estritamente maior** que o terceiro lado; lados devem ser positivos.

### Evidência de cobertura — Exercício 1 (Triângulo)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/pablo-cunha/Documentos/Fatec/5º Semestre/Nadalete/TDD
plugins: cov-7.1.0
collected 15 items

test_geometry.py ...............                                         [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name          Stmts   Miss  Cover   Missing
-------------------------------------------
geometry.py      16      0   100%
-------------------------------------------
TOTAL            16      0   100%
============================== 15 passed in 0.06s ==============================
```

**Cobertura: 100%** em `geometry.py` (16 statements, 0 missing).

---

# Exercício 2 — PersonDAO.isValidToInclude() (TDD)

Valida um objeto `Person` e retorna uma lista de erros. Regras:

- Nome com ao menos 2 partes, apenas letras
- Idade no intervalo [1, 200]
- Pelo menos um `Email` associado
- Cada e-mail no formato `_____@_____._____` (cada parte com ao menos 1 caractere)

Classes: `Person`, `Email`, `PersonDAO` em `person.py`.

### Evidência de cobertura — Exercício 2 (PersonDAO)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/pablo-cunha/Documentos/Fatec/5º Semestre/Nadalete/TDD
plugins: cov-7.1.0
collected 29 items

test_geometry.py ...............                                         [ 51%]
test_person.py ..............                                            [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name          Stmts   Miss  Cover   Missing
-------------------------------------------
geometry.py      16      0   100%
person.py        29      1    97%   28
-------------------------------------------
TOTAL            45      1    98%
============================== 29 passed in 0.08s ==============================
```

**Cobertura: 97%** em `person.py` (29 statements, 1 missing — linha 28 é o stub de `save()`, fora do foco deste exercício). `isValidToInclude()` coberto integralmente.

---

# Exercício 3 — Calculadora de Salário (TDD)

Calcula o salário líquido de um `Funcionario` (nome, email, salário-base, cargo) conforme o cargo:

| Cargo | Limiar | Desconto (>= limiar) | Desconto (< limiar) |
|-------|--------|----------------------|---------------------|
| DESENVOLVEDOR | 3000 | 20% | 10% |
| DBA | 2000 | 25% | 15% |
| TESTADOR | 2000 | 25% | 15% |
| GERENTE | 5000 | 30% | 20% |

Classes: `Cargo`, `Funcionario`, `CalculadoraSalario` em `salary.py`.

### Evidência de cobertura — Exercício 3 (Calculadora de Salário)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/pablo-cunha/Documentos/Fatec/5º Semestre/Nadalete/TDD
plugins: cov-7.1.0
collected 39 items

test_geometry.py ...............                                         [ 38%]
test_person.py ..............                                            [ 74%]
test_salary.py ..........                                                [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name          Stmts   Miss  Cover   Missing
-------------------------------------------
geometry.py      16      0   100%
person.py        29      1    97%   28
salary.py        18      0   100%
-------------------------------------------
TOTAL            63      1    98%
============================== 39 passed in 0.14s ==============================
```

**Cobertura: 100%** em `salary.py` (18 statements, 0 missing).
