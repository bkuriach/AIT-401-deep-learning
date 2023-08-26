'''
Write program to check whether input is an Armstrong number or not.
An Armstrong number is a number that is equal to the sum of its digits 
raised to the power of the number of digits. For example, 153 is an 
Armstrong number because 1^3 + 5^3 + 3^3 = 153
'''

class ArmstrongNumber:
    def is_amstrong_number(self, number):
        num_digits = len(str(number))
        sum = 0
        for digit in str(number):
            sum += int(digit) ** num_digits
        if sum == number:
            return True
        return False
    

obj = ArmstrongNumber()
obj.is_amstrong_number(153)
obj.is_amstrong_number(1634)
obj.is_amstrong_number(1635)
