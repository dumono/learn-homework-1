"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""

def hello_user():
    """
    Замените pass на ваш код
    """
    ans = ""
    while ans != "Хорошо":
        ans = str(input("Как дела? ")).capitalize()


if __name__ == "__main__":
    hello_user()
