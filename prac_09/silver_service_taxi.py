from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi Class"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize Instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness