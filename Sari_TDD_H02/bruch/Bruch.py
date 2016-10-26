from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """
    Bruch Klasse
    (Diese Klasse wurde nach den Testfaellen erstellt.)

    __version__ = '1.0'
    __author__ = 'Yunus Sari'
    """

    def __init__(self, zaehler=0, nenner=1):
        """
        Konstruktor

        :param zaehler:
        :param nenner:
        :raises TypeError: "falscher Typ",
        :raises ZeroDivisionError: Divison 0
        """
        if type(zaehler) is Bruch:
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('falscher Typ:')
        elif type(nenner) is not int:
            raise TypeError('falscher Typ:')
        if nenner == 0:
            raise ZeroDivisionError('Division 0')
        self.zaehler = zaehler
        self.nenner = nenner

    def __radd__(self, zaehler):
        """
        Additon
        Kann mit einer Zahl oder einem Bruch addiert werden

        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        return self.__add__(zaehler)

    
    def __add__(self, zaehler):
        """
        Addition
        Wird automatisch ein Bruch mit einer 1 im Nenner

        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('falsche Typen:')
        else:
            b1 = Bruch(zaehler) # Falls ganzzahlig ==> Nenner = 1 (Konstrutkor)
        return Bruch(self.nenner*b1.zaehler+self.zaehler*b1.nenner, self.nenner*b1.nenner)

    def __iadd__(self, other):
        """
        Bruch wird mit dem selben Bruch addiert

        :param other: Bruch
        :return: self
        """
        return self.__add__(other)
 
    def __rsub__(self, left):
        """
        Subtraktion
        Kann mit einer Zahl oder einem Bruch subrahiert werden

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(left) == int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('falche Typen:')

    def __sub__(self, zaehler):
        """
        Subtraktion
        Wird automatisch ein Bruch mit einer 1 im Nenner

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('falsche Typen:')
        else:
            b1 = Bruch(zaehler) # Falls ganzzahlig ==> Nenner = 1 (Konstrutkor)
        return Bruch(self.zaehler*b1.nenner-b1.zaehler*self.nenner, self.nenner*b1.nenner)

    def __isub__(self, other):
        """
        Bruch wird mit dem selben Bruch subrahiert

        :param other: Bruch
        :return: self
        """
        return self.__sub__(other)

    def __rmul__(self, zaehler):
        """
        Multiplikation
        Kann mit einer Zahl oder einem Bruch addiert werden

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        return self.__mul__(zaehler)
    
    def __mul__(self, zaehler):
        """

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('falsche Typen:')
        else:
            b1=Bruch(zaehler)
        z2 = b1.zaehler*self.zaehler
        n2 = b1.nenner*self.nenner
        return Bruch(z2, n2)

    def __imul__(self, other):
        """
        Bruch wird mit dem selben Bruch multipliziert

        :param other: other Bruch
        :return: self
        """
        return self.__mul__(other)

    def __rtruediv__(self, left):
        """
        Division
        Kann mit einer Zahl oder einem Bruch dividiert werden

        :param zaehler: int oder Bruch
        :return: Bruch
        :raises TypeError: falsche Typen
        :raises ZeroDivisionError: Division 0
        """
        if type(left) is not Bruch and type(left) is not int:
            raise TypeError('falsche Typen:')
        elif self.zaehler == 0:
            raise ZeroDivisionError('Division 0')
        else:
            b1 = Bruch(left)
            return Bruch(self.nenner * b1.zaehler, self.zaehler)

    def __truediv__(self, zaehler):
        """
        Eine Division durch eine ganze Zahl oder einem Bruch

        :param zaehler: Bruch oder int
        :return: Bruch
        :raises TypeError: falsche Typen
        :raises ZeroDivisionError: Division 0
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('falsche Typen:')
        b1 = Bruch(zaehler)
        if b1.zaehler == 0:
            raise ZeroDivisionError('Division 0')
        return self.__mul__(Bruch(b1.nenner, b1.zaehler))

    def __pow__(self, exp):
        """
        Potenz eines Bruches

        :param int exp: Exponent
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(exp) is int:
            return Bruch(self.zaehler ** exp, self.nenner ** exp)
        else:
            raise TypeError('falsche Typen')

    def __invert__(self):
        """
        Invertration eines Bruches

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        Überschreibung der Stringfunktion

        :return str: Ausgabe
        """

        gcd = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler = self.zaehler/gcd
        self.nenner = self.nenner/gcd

        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler

        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(other):
        """
        Erstellung eines Bruches

        :param other: Bruch oder int
        :return: Bruch
        :raise TypeError: falsche Typen
        """
        if type(other) is Bruch:
            return other
        elif type(other) is int:
            b1 = Bruch(other, 1)
            return b1
        else:
            raise TypeError('falsche Typen')

    def __eq__(self, other):
        """
        Schaut ob beide Brüche gleich (equal) sind

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()==other.__float__()


    def __ne__(self, other):
        """
        Schaut ob beide Brüche nicht gleich (equal) sind

        :param other: anderer Bruch
        :return: boolean
        """
        return not self.__eq__(other)




    def __abs__(self):
        """
        Absoluter Wert des Bruches

        :return: positiver Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __itruediv__(self, other):
        """
        Division mit sich selber

        :param other: anderer Bruch
        :return: self
        """
        return self.__truediv__(other)

    def __float__(self):
        """
        Override float()

        :return: float
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        Override int()

        :return: int
        """
        return int(self.__float__())

    def __complex__(self):
        """
        Override complex()

        :return: complex
        """
        return complex(self.__float__())

    def __neg__(self):
        """
        Bruch wird negativ

        :return:  negatiever Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __gt__(self, other):
        """
        Vergleich
        Groesser als

        :param other: anderer Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.__float__()> other.__float__()

    def __lt__(self, other):
        """
        Vergleich
        Kleiner als

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__() < other.__float__()

    def __ge__(self, other):
        """
        Vergöeich
        Groesser gleich

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()>= other.__float__()


    def __le__(self, other):
        """
        Vergleich
        Kleiner gleich

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()<= other.__float__()

    @classmethod
    def gcd(cls, x, y):
        """
        Euklidscher Algorithmus

        :param int x: erster Wert
        :param int y: zweiter Wert
        :return: groesster gemeinsamer Teiler
        """
        x, y = abs(x), abs(y)
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __iter__(self):
        """
        Itarable Klasse
        """
        return (self.zaehler, self.nenner).__iter__()