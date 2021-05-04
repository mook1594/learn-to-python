import random
from multiprocessing.pool import Pool

def prime_factor(value):
    factors = []
    for divisor in range(2, value-1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor))
            factors.extend(prime_factor(quotient))
            break
        else:
            factors = [value]
    return factors

if __name__ == '__main__':
    pool = Pool()

    to_factor = [
        random.randint(100_000, 500_000_000) for i in range(20)
    ]

    results = pool.map(prime_factor, to_factor)

    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factors))

# from multiprocessing import Process, cpu_count
# import time
# import os
#
# class MuchCPU(Process):
#     def run(self):
#         print(os.getpid())
#         for i in range(200_000_000):
#             pass
#
# if __name__ == '__main__':
#     process = [MuchCPU() for f in range(cpu_count)]
#     t = time.time()
#     for p in process:
#         p.start()
#     for p in process:
#         p.join()
#
#     print('work took {} seconds'.format(time.time() - t))
