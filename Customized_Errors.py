class RuntimeErrorWithCode(Exception):
    """
    Exception raised whem a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code

er=RuntimeErrorWithCode('An error happened.',500)
print(er.__doc__)





class UncountableError(ValueError):
    def __init__(self,wrong_value):
        super().__init__('Invalid value for n, {}. n must be greater than 0.'.format(wrong_value))

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)

count_from_zero_to_n(20)
