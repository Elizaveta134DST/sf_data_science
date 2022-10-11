import numpy as np

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

def random_predict(number:int=1)-> int:
    
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_n = 1 # минимальное значение интервала
    max_n = 101 # максимальное значение интервала
    md = 0
    predict_number = int(np.random.randint(1, 101))
    
    while predict_number != number:
        count += 1
        if predict_number > number:
           max_n = predict_number
           predict_number = (max_n + min_n) // 2
           # "разделяем и властвуем" с помощью бинарного поиска
           
        elif predict_number < number:
           min_n = predict_number
           predict_number = (max_n + min_n) // 2
        else:
            break #выход, если угадали
    return count

def score_game(random_predict) -> int:
    
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(int(random_predict(number)))
    score =int(np.mean(count_ls))
    print(f'ваш алгоритм угадывает в среднем за: {score} попыток')
    return(score)
print(f'количество попыток: {random_predict(10)}')

#RUN
if __name__=="_main_":
    score_game(random_predict) 