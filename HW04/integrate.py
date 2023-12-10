import concurrent.futures
import logging
import math
import multiprocessing
import time

logging.basicConfig(
    filename="integrate.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def worker_integrate(f, a, b, step):
    acc = 0
    for i in range(a, b):
        acc += f(i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, executor_type="ThreadPoolExecutor"):
    logging.info(f"Integration started with {n_jobs} workers")

    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    tasks = []

    for i in range(0, n_jobs):
        start = i * chunk_size
        end = (i + 1) * chunk_size

        if i == n_jobs - 1:
            end = n_iter

        tasks.append((start, end))

    result = 0

    if n_jobs == 1:
        result = worker_integrate(f, 0, n_iter, step)
    else:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(worker_integrate, f, start, end, step)
                for start, end in tasks
            ]
            for future in concurrent.futures.as_completed(futures):
                try:
                    result += future.result()
                except Exception as e:
                    logging.error(f"Exception encountered during execution: {e}")

    logging.info("Integration completed")
    return result


def measure_executor_time(executor_type, n_jobs_range):
    results = []
    for n_jobs in n_jobs_range:
        start = time.perf_counter()
        result = integrate(
            math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type=executor_type
        )
        end = time.perf_counter()
        elapsed = end - start
        results.append((n_jobs, elapsed))
        print(f"{executor_type} with {n_jobs} workers: {elapsed:.2f} sec")
    return results


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    n_jobs_range = range(1, cpu_num * 2 + 1)

    print("ThreadPoolExecutor results:")
    thread_results = measure_executor_time("ThreadPoolExecutor", n_jobs_range)

    print(
        "\nChanging executor_type in the integrate function to 'ProcessPoolExecutor':"
    )
    with open("integrate.log", "a") as f:
        f.write("\n\n")

    def integrate(
        f, a, b, *, n_jobs=1, n_iter=1000, executor_type="ThreadPoolExecutor"
    ):
        logging.info(f"Integration started with {n_jobs} workers")

        step = (b - a) / n_iter
        chunk_size = n_iter // n_jobs
        tasks = []

        for i in range(0, n_jobs):
            start = i * chunk_size
            end = (i + 1) * chunk_size

            if i == n_jobs - 1:
                end = n_iter

            tasks.append((start, end))

        result = 0

        if n_jobs == 1:
            result = worker_integrate(f, 0, n_iter, step)
        else:
            with concurrent.futures.ProcessPoolExecutor() as executor:
                futures = [
                    executor.submit(worker_integrate, f, start, end, step)
                    for start, end in tasks
                ]
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result += future.result()
                    except Exception as e:
                        logging.error(f"Exception encountered during execution: {e}")

        logging.info("Integration completed")
        return result

    print("ProcessPoolExecutor results:")
    process_results = measure_executor_time("ProcessPoolExecutor", n_jobs_range)
