class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input("Enter a number: "))

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is greater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)


#Your code is using a custom exception, CustomException, to handle cases where the input is either less than 10 or greater than 10.
#It's a good use of custom exceptions to provide more specific information about the nature of the error. 
#However, there's a small typo in the raise CustomException("Input is grater than 10") line (it should be "greater" instead of "grater").
