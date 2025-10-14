# currency.py

class Currency:
    """A very simple Currency class for educational purposes."""

    # Let's pretend 1 USD = 0.92 EUR (just a static conversion rate)
    CONVERSION_RATES = {
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09
    }

    def __init__(self, amount, code="USD"):
        self.amount = float(amount)
        self.code = code.upper()

    # ---------- Representation ----------
    def __repr__(self):
        return f"{self.amount:.2f} {self.code}"

    # ---------- Arithmetic ----------
    def __add__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            return Currency(self.amount + other.amount, self.code)
        raise TypeError("Can only add Currency of same type")

    def __sub__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            return Currency(self.amount - other.amount, self.code)
        raise TypeError("Can only subtract Currency of same type")

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            self.amount += other.amount
            return self
        raise TypeError("Can only add Currency of same type")

    def __isub__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            self.amount -= other.amount
            return self
        raise TypeError("Can only subtract Currency of same type")

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Currency(self.amount * value, self.code)
        raise TypeError("Can only multiply by a number")

    def __truediv__(self, value):
        if isinstance(value, (int, float)) and value != 0:
            return Currency(self.amount / value, self.code)
        raise TypeError("Can only divide by a non-zero number")

    # ---------- Comparison ----------
    def __le__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            return self.amount <= other.amount
        raise TypeError("Can only compare Currency of same type")

    def __ge__(self, other):
        if isinstance(other, Currency) and self.code == other.code:
            return self.amount >= other.amount
        raise TypeError("Can only compare Currency of same type")

    # ---------- Type Conversions ----------
    def __int__(self):
        return int(self.amount)

    def __float__(self):
        return float(self.amount)

    # ---------- Non-special method ----------
    def convert_to(self, target_code):
        """Convert this currency to another predefined type."""
        target_code = target_code.upper()
        key = (self.code, target_code)
        if key in self.CONVERSION_RATES:
            new_amount = self.amount * self.CONVERSION_RATES[key]
            return Currency(new_amount, target_code)
        raise ValueError(f"No conversion rate from {self.code} to {target_code}")
