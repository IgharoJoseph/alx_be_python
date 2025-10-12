class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method:
        Performs addition without needing access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method:
        Accesses class-level data using 'cls' and performs multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
