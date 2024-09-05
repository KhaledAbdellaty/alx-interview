#!/usr/bin/python3


def isWinner(x, nums):
    """
    This function determines the winner of the prime
    number game based on Maria and Ben's optimal strategies.

    Args:
        x (int): The number of rounds in the game.
        nums (list): A list of integers representing
        the starting set of numbers for each round.

    Returns:
        str or none: A string indicating the winner
        ("Maria", "Ben", or "None" if winner cannot be determined),
        or None if there's a tie or invalid input.
    """
    def sieve_of_eratosthenes(n):
        """
        This function implements the Sieve of Eratosthenes algorithm
        to efficiently generate a list of prime numbers up to n.

        Args:
            n (int): The upper limit of the range to check for primes.

        Returns:
            list: A boolean list where True at index i
            indicates that i is prime.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def determine_winner(n):
        """
        Determine the winner of a single game with maximum number n.

        Args:
            n (int): The maximum number for the game round.

        Returns:
            str: The name of the winner ("Maria" or "Ben") for this round.

        Note:
        This function assumes optimal play from both players.
        """
        primes = sieve_of_eratosthenes(n)
        prime_count = sum(primes)
        return "Maria" if prime_count % 2 == 1 else "Ben"

    if not nums or x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
