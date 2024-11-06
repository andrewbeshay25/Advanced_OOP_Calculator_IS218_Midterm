from abc import ABC, abstractmethod
from app.operations import addition, subtraction, multiplication, division, Number

class Calculation(ABC):
    """
    Abstract base class representing a mathematical calculation.
    
    This class defines the structure for any arithmetic operation, requiring subclasses
    to implement the `compute`, `__str__`, and `__repr__` methods. 

    Attributes:
    a (Number): The first operand (can be int or float).
    b (Number): The second operand (can be int or float).
    """

    def __init__(self, a: Number, b: Number) -> None:
        """
        Initialize the operands for the calculation.

        Args:
        a (Number): First operand.
        b (Number): Second operand.

        Raises:
        TypeError: If 'a' or 'b' are not of type int or float.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be numbers (int or float)")
        self.a = a
        self.b = b

    @classmethod
    def create(cls, a: Number, b: Number) -> 'Calculation':
        """
        Factory method to create a new Calculation instance.

        Args:
        a (Number): First operand.
        b (Number): Second operand.

        Returns:
        Calculation: A new instance of the calculation.
        """
        return cls(a, b)

    @abstractmethod
    def compute(self) -> Number:
        """
        Abstract method to compute the result of the calculation.
        
        Must be implemented by any subclass.

        Returns:
        Number: The result of the calculation.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method to return a user-friendly string representation.

        Returns:
        str: The formatted string representation of the operation.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method to return a detailed representation for debugging.

        Returns:
        str: A detailed representation of the operation.
        """
        pass

class Addition(Calculation):
    """
    Represents an addition operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return addition(self.a, self.b)

    def __str__(self) -> str:
        return f"Addition: {self.a} + {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Addition(a={self.a}, b={self.b}, result={self.compute()})"

class Subtraction(Calculation):
    """
    Represents a subtraction operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return subtraction(self.a, self.b)

    def __str__(self) -> str:
        return f"Subtraction: {self.a} - {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Subtraction(a={self.a}, b={self.b}, result={self.compute()})"

class Multiplication(Calculation):
    """
    Represents a multiplication operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return multiplication(self.a, self.b)

    def __str__(self) -> str:
        return f"Multiplication: {self.a} * {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Multiplication(a={self.a}, b={self.b}, result={self.compute()})"

class Division(Calculation):
    """
    Represents a division operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        if self.b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return division(self.a, self.b)

    def __str__(self) -> str:
        result = self.compute()
        # If the result is a whole number, format it as an integer; otherwise, keep it as a float.
        formatted_result = int(result) if result.is_integer() else result
        return f"Division: {self.a} / {self.b} = {formatted_result}"

    def __repr__(self) -> str:
        result = self.compute()
        formatted_result = int(result) if result.is_integer() else result
        return f"Division(a={self.a}, b={self.b}, result={formatted_result})"