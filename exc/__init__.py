class ArgumentError(Exception):
    """Exception raised for errors in the passed arguments.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.message = message
