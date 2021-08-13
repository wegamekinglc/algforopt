from concurrent.futures import ProcessPoolExecutor
import numpy as np


def sub_func():
    values = np.random.randn(20000000)
    total_values = np.sum(values)


def main():
    tasks = []
    with ProcessPoolExecutor(max_workers=16) as pool:
        for i in range(1, 501):
            t = pool.submit(sub_func)
            tasks.append(t)

    for t in tasks:
        t.result()


if __name__ == "__main__":
    import datetime as dt
    start = dt.datetime.now()
    main()
    print(dt.datetime.now() - start)
