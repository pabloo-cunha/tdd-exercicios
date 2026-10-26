import re


class Email:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Person:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        emails: list[Email] | None = None,
    ):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails if emails is not None else []


class PersonDAO:
    _EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def save(self, p: Person) -> None:
        pass

    def isValidToInclude(self, p: Person) -> list[str]:
        errors: list[str] = []

        parts = p.name.split()
        if len(parts) < 2 or not all(part.isalpha() for part in parts):
            errors.append("Nome inválido")

        if p.age < 1 or p.age > 200:
            errors.append("Idade inválida")

        if not p.emails:
            errors.append("Person deve ter ao menos um email")
        else:
            for email in p.emails:
                if not self._EMAIL_PATTERN.match(email.name):
                    errors.append("Email inválido")
                    break

        return errors
