from person import Email, Person, PersonDAO


def _pessoa_valida(**overrides) -> Person:
    defaults = {
        "id": 1,
        "name": "Ada Lovelace",
        "age": 36,
        "emails": [Email(1, "a@b.c")],
    }
    defaults.update(overrides)
    return Person(**defaults)


def test_pessoa_valida_retorna_lista_vazia():
    erros = PersonDAO().isValidToInclude(_pessoa_valida())
    assert erros == []


def test_nome_com_uma_parte():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(name="Ada"))
    assert "Nome inválido" in erros


def test_nome_com_caracteres_nao_letra():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(name="Ada Lovelace2"))
    assert "Nome inválido" in erros


def test_idade_menor_que_um():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(age=0))
    assert "Idade inválida" in erros


def test_idade_maior_que_duzentos():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(age=201))
    assert "Idade inválida" in erros


def test_idade_limite_inferior_valido():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(age=1))
    assert "Idade inválida" not in erros
    assert erros == []


def test_idade_limite_superior_valido():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(age=200))
    assert "Idade inválida" not in erros
    assert erros == []


def test_sem_emails():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[]))
    assert "Person deve ter ao menos um email" in erros


def test_email_sem_arroba():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[Email(1, "abc.def")]))
    assert "Email inválido" in erros


def test_email_sem_ponto_no_dominio():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[Email(1, "a@bc")]))
    assert "Email inválido" in erros


def test_email_parte_local_vazia():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[Email(1, "@b.c")]))
    assert "Email inválido" in erros


def test_email_parte_dominio_vazia():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[Email(1, "a@.c")]))
    assert "Email inválido" in erros


def test_email_parte_tld_vazia():
    erros = PersonDAO().isValidToInclude(_pessoa_valida(emails=[Email(1, "a@b.")]))
    assert "Email inválido" in erros


def test_multiplos_erros():
    pessoa = Person(1, "Ada", 0, [])
    erros = PersonDAO().isValidToInclude(pessoa)
    assert "Nome inválido" in erros
    assert "Idade inválida" in erros
    assert "Person deve ter ao menos um email" in erros
    assert len(erros) == 3
