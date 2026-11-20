
print()
print("Стратегия")
print()

from abc import *

class TextFormatter(ABC):
    @abstractmethod
    def format_text(self, s: str):
        pass
class UpperCaseFormatter(TextFormatter):
    def format_text(self, s: str):
        s = s.upper()
        return s

class TitleFormatter(TextFormatter):
    def format_text(self, s: str):
        s = s.title()
        return s

class TextEditor:
    def __init__(self, formatter):
        self.formatter = formatter

    def set_formatter(self, formatter):
        self.formatter = formatter

    def publish(self, s: str):
        print(self.formatter.format_text(s))


editor = TextEditor(UpperCaseFormatter())
editor.publish("Текст в апперкейсе")

editor.set_formatter(TitleFormatter())
editor.publish("текст в тайтл формате")


print()
print("Цепочка обязанностей")
print()

from abc import *
class Payment:
    def __init__(self, payment_type: str, amount: int):
        self.payment_type = payment_type
        self.amount = amount


class PayHandler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def can_pay(self, payment):
        pass

    def pay(self, payment):
        if self.can_pay(payment):
            return f"Платеж проведен обработчиком {self.__class__.__name__}"
        if self._next_handler is not None:
            return self._next_handler.pay(payment)
        return "Платеж не проведен"


class CashHandler(PayHandler):
    def can_pay(self, payment: Payment):
        return payment.payment_type == "cash" and payment.amount <= 500


class CardHandler(PayHandler):
    def can_pay(self, payment: Payment):
        return payment.payment_type == "card" and payment.amount >= 1000

card_handler = CardHandler()
cash_handler = CashHandler(next_handler=card_handler)
handler = cash_handler

payment = Payment(payment_type='card', amount=1000)
print(handler.pay(payment))

payment = Payment(payment_type='cash', amount=500)
print(handler.pay(payment))

payment = Payment(payment_type='card', amount=780)
print(handler.pay(payment))


print()
print("Итератор")
print()

class ReverseBookIterator:
    def __init__(self, pages):
        self._pages = pages
        self._index = len(pages) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        page = self._pages[self._index]
        self._index -= 1
        return page

class Book:
    def __init__(self, title, pages):
        self.title = title
        self._pages = pages

    def __iter__(self):
        return iter(self._pages)

    def reversed_pages(self):
        return ReverseBookIterator(self._pages)

book = Book("(НазваниеКниги)", ["стр.1", "стр.2", "стр.3"])

print("Прямой обход:")
for page in book:
    print(page)

print()

print("Обратный обход:")
for page in book.reversed_pages():
    print(page)
