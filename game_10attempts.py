"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 10 попыток
"""
import numpy as np

def random_predict(number: int = 1) -> int:
    """Функция для самостояльного поиска угадываемого числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min = 1
    max = 100
    middle = round((max+min)/2)
    count = 1
    # напишем цикл для поиска варианта
    while middle != number:
        count +=1
        if middle > number:
            max = middle -1
            middle = round((max+min)/2)
        else:
            min = middle +1
            middle = round((max+min)/2)      
    
    return count 
  
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []

    # np.random.seed(1)

    random_array = np.random.randint(1, 101, size =(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток. Это число: {number}")



if __name__ == "__main__":
    score_game(random_predict)