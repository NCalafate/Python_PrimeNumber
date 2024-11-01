> IPS - Escola Superior de Tecnologia de Setúbal
>
> LEI - Computação Paralela e Distribuída 2023 / 2024


# Trabalho Prático #1 – Números primos grandes

## Código

### is_prime

Prime numbers, except for 2 and 3, follow a unique pattern: they can be expressed as 6n±1. To check if a number is prime, we start with 5 and then add or subtract 6 at each step. This approach helps avoid calculating numbers that are multiples of 2 or 3, making the process more efficient.
[Source](https://en.wikipedia.org/wiki/Primality_test)

### find_max_prime

This function iterates through odd numbers, starting from a value greater than the current largest prime number. It checks each odd number for primality using the `is_prime` function and updates the largest prime number if it finds a higher one.

### main

**Simplified process description:**

1. Receive parameters from the user
2. Initialize shared memory objects
3. Initialize processes with the `find_max_prime` function and the arguments `max_prime` and `lock`
4. Group processes into a list for easy iteration
5. Run the processes
6. Wait for a time defined by the user
7. Terminate the processes
8. Display the largest prime number found
9. Repeat steps 2 to 8 according to the number of executions specified

## Results

### Reference Solution

Macbook Pro CPU 2,4 GHz Intel Core i5 – Dual Core

| #PROC | TIME | PRIME               | LENGHT |
|-------|------|---------------------|--------|
| 4     | 5s   | 31005333773915239   | 17     |
| 4     | 20s  | 672578069018335093  | 18     |
| 8     | 20s  | 400319213016733573  | 18     |
| 4     | 60s  | 3171951615452780311 | 19     |
| 8     | 60s  | 361590838463309249  | 18     | 

### Implemented Solution

Windows 11 CPU 3,7 GHz AMD Ryzen 5 5600X – Hexa Core

| #PROC | TIME | PRIME               | LENGHT |
|-------|------|---------------------|--------|
| 4     | 5s   | 58419509909260933   | 17     |
| 4     | 20s  | 1045537756226118937 | 19     |
| 8     | 20s  | 670883517857260297  | 18     |
| 4     | 60s  | 2003244016827530167 | 19     |
| 8     | 60s  | 2486558838502971781 | 19     | 

Note: Best result out of 10 executions