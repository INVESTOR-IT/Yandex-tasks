from time import process_time_ns

import first_solution
import second_solution


def function_operation_time(func):

    def wrapper(*args, **kwargs):
        start = process_time_ns()
        result_func = func(*args, **kwargs)
        end = process_time_ns()
        result = (f'Результат {func.__name__}\n'
                  f'Входные данные {args}\n'
                  f'Время работы {end - start} наносекунд\n')
        return result

    return wrapper


@function_operation_time
def first_option(n, k):
    result = first_solution.friends_and_Jan_on_track(n, k)
    return first_solution.output_left_and_right_borders(*result)


@function_operation_time
def second_option(n, k):
    result = second_solution.friends_and_Jan_on_track(n, k)
    return second_solution.output_left_and_right_borders(*result)


# Тест с малом количеством друзей
print(first_option(100, 20))
print(second_option(100, 20))

# Тест с средним количеством друзей
print(first_option(100, 30))
print(second_option(100, 30))

# Тест с большим количеством друзей
print(first_option(100, 90))
print(second_option(100, 90))
