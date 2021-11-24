"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def sold_summ(stock):
    summ = 0
    for price in stock:
        summ += price
    return summ

def sold_average(stock):
    summ = sold_summ(stock)
    return summ / len(stock)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

    summ_all = 0
    count_all = 0
    for item in stock:
        product = item['product']
        sold_s = sold_summ(item['items_sold'])
        avr = sold_average(item['items_sold'])
        print(f'''{product}: \nсумма продаж:\t{sold_s}
среднее количество продаж:\t {avr}\n''')
        summ_all += sold_s
        count_all += len(item['items_sold'])
    print(f'суммарное количество продаж всех товаров: {summ_all}')
    print(f'среднее количество продаж всех товаров: {summ_all / count_all}')


if __name__ == "__main__":
    main()
