import multiprocessing
import threading
import time


# Функция для вычисления числа Фибоначчи
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = 35

# Синхронный запуск
start = time.perf_counter()
for _ in range(10):
    result = fib(n)
end = time.perf_counter()
print(f"Синхронный запуск: {end - start:.2f} сек.")

# Использование потоков
result = []
start = time.perf_counter()


def threaded_fib():
    result.append(fib(n))


threads = [threading.Thread(target=threaded_fib) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"Запуск с использованием потоков: {end - start:.2f} сек.")

# Использование процессов
n = 35
result = multiprocessing.Manager().list([])
start = time.perf_counter()


def process_fib(n, result):
    result.append(fib(n))


processes = [
    multiprocessing.Process(target=process_fib, args=(n, result)) for _ in range(10)
]

for process in processes:
    process.start()

for process in processes:
    process.join()

end = time.perf_counter()
print(f"Запуск с использованием процессов: {end - start:.2f} сек.")
