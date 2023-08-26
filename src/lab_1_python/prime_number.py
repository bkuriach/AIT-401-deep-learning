'''
Write program to check whether input is a prime number or not.
'''
class PrimeNumber:
    def is_prime_number(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5)+1):
            if number % i == 0:
                return False
        return True

obj = PrimeNumber()
obj.is_prime_number(2)
obj.is_prime_number(3)
obj.is_prime_number(4)
obj.is_prime_number(5)
obj.is_prime_number(6)
obj.is_prime_number(7)
obj.is_prime_number(127)
