class Order:
    def __init__(self, customer: str, city: str,
                 address: str, tel_num: int, volume: str,
                 brand: str, aroma: str):
        self.city = city
        self.customer = customer
        self.address = address
        self.tel_num = tel_num
        self.volume = volume
        self.brand = brand
        self.aroma = aroma
        self._promo_code = ''
        self._message = ''

    def __str__(self):
        return f'Новый заказ от {self.customer}. Город: {self.city}, Адрес: {self.address}, номер: {self.tel_num},' \
               f' объем: {self.volume}, бренд: {self.brand}, аромат: {self.aroma},' \
               f' промокод: {self._promo_code}, сообщение: {self._message}'

    @property
    def promo_code(self):
        return self._promo_code

    @promo_code.setter
    def promo_code(self, a):
        self._promo_code = a

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, a):
        self._message = a
