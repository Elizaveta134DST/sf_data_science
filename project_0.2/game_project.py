import numpy as np

def random_predict(number:int=1)-> int:
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
        elif predict_number < number:
           min_n = predict_number
           predict_number = (max_n + min_n) // 2
        else:
            break
    return count

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(int(random_predict(number)))
    score =int(np.mean(count_ls))
    print(f'ваш алгоритм угадывает в среднем за: {score} попыток')
    return(score)
print(f'количество попыток: {random_predict(10)}')
score_game(random_predict) 