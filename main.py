import multiprocessing
import random
import time
from math import isqrt

""" INFO
    Instituto Politécnico De Setúbal
        Escola Superior de Tecnologia de Setúbal
            Licenciatura em Engenharia Informática
                Computação Paralela e Distribuída 2023 / 2024
                    Trabalho Prático #1 – Números primos grandes
 """

""" REFERENCE SOLUTION
    #Proc.  Time    Prime
    4       5s      31005333773915239    (17)
    4       20s     672578069018335093   (18)
    8       20s     400319213016733573   (18)
    4       60s     3171951615452780311  (19)
    8       60s     361590838463309249   (18) """

""" IMPLEMENTED SOLUTION (highest in 10 executions)
    #Proc.  Time    Prime
    4		5s		58419509909260933    (17)
    4	 	20s     1045537756226118937  (19)
    8	 	20s     670883517857260297   (18)
    4		60s     2003244016827530167  (19)
    8		60s     2486558838502971781  (19) """


def is_prime(n: int) -> bool:
    """ Checks if a number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Explanation:
        Prime numbers, except for 2 and 3, have a special pattern: they can be written as either 6 times some number plus 1, or 6 times some number minus 1. \n
        To check if a number is prime, we first check if it's 2 or 3. If it's not, then we start checking higher numbers in pairs.\n
        We begin with 5, then check 7, then 11, and so on, always adding or subtracting 6 from the previous number.\n
        Within each pair, we only check two numbers apart, which helps us avoid checking multiples of 2 or 3. This method helps us efficiently find prime numbers without unnecessary calculations.

    Source:
        https://en.wikipedia.org/wiki/Primality_test """

    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def find_max_prime(max_prime, lock):
    """ Finds and updates the maximum prime number.

        Parameters:
            max_prime (multiprocessing.Value): Shared value representing the maximum prime found.
            lock (multiprocessing.Lock): Lock for synchronization in multiprocessing.

        Explanation:
            This function iterates through odd numbers, starting from a value greater than the current maximum prime number.
            It checks each odd number for primality using the is_prime function and updates the maximum prime number if a larger one is found. """

    current_number = 1

    while True:

        p_max_prime = max_prime.value

        if current_number <= p_max_prime:
            current_number = random.randrange(p_max_prime, p_max_prime * 100, 2)

        if is_prime(current_number) and current_number > p_max_prime:
            with lock:
                if current_number > max_prime.value:
                    max_prime.value = current_number

        current_number += 2


if __name__ == '__main__':
    print("> Welcome to the Find Max Prime script!")
    print("| This script aims to discover the highest prime number based on the provided parameters.")
    print("| Kindly specify the number of processes to utilize, the timeout duration and the execution count.")
    print("| Invalid input will run the program with default parameters.\n")

    """ SETUP """
    try:
        num_processes = int(input("« Processes: "))
        timeout = int(input("« Timeout: "))
        executions = int(input("« Executions: "))
    except ValueError:
        num_processes = 4
        timeout = 5
        executions = 1
        print(f"\n> Invalid Input, ")
        print(f"| Starting with default parameters:")
        print(f"| - Processes: {num_processes}")
        print(f"| - Timeout: {timeout}")
        print(f"| - Executions: {executions}")

    with multiprocessing.Manager() as manager:

        print(f"\n> Results:\n|  ##\tPrime")

        for n_exec in range(executions):

            """ INITIALIZATION """
            max_prime = manager.Value('i', 3)
            lock = multiprocessing.Lock()
            process_list = list()

            for _ in range(num_processes):
                process = multiprocessing.Process(target=find_max_prime, args=[max_prime, lock])
                process_list.append(process)

            """ START PROCESS """
            for p in process_list:
                p.start()

            time.sleep(timeout)

            """ END PROCESS """
            for p in process_list:
                p.terminate()
                p.join()

            """ SHOW RESULT """
            print(f"|  {n_exec + 1}\t{max_prime.value} ({len(str(max_prime.value))})")
