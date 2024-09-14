from abc import ABC, abstractmethod

class Phone(ABC):

    def __init__(self, brand, model, color, storage, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage
        self.price = price

    @abstractmethod
    def make_call(self, number):
        pass

    @abstractmethod
    def send_message(self, number, message):
        pass

    def get_info(self):
        info = f"Марка: {self.brand}n"
        info += f"Модель: {self.model}n"
        info += f"Цвет: {self.color}n"
        info += f"Память: {self.storage} ГБn"
        info += f"Цена: {self.price}"
        return info


class IPhone(Phone):

    def __init__(self, model, color, storage, price, os_version):
        super().__init__("Apple", model, color, storage, price)
        self.os_version = os_version

    def make_call(self, number):
        print(f"Звоню на номер {number} с IPhone {self.model}.")

    def send_message(self, number, message):
        print(f"Отправляю сообщение на номер {number}: {message} с IPhone {self.model}.")


class Android(Phone):

    def __init__(self, brand, model, color, storage, price, android_version):

        super().__init__(brand, model, color, storage, price)
        self.android_version = android_version

    def make_call(self, number):
        print(f"Звоню на номер {number} с Android-устройства {self.brand} {self.model}.")

    def send_message(self, number, message):
        print(f"Отправляю сообщение на номер {number}: {message} с Android-устройства {self.brand} {self.model}.")


class IPhone15(IPhone):

    def __init__(self, model, color, storage, price, os_version, serial_number):
        super().__init__(model, color, storage, price, os_version)
        self.serial_number = serial_number

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number


class IPhone4(IPhone):

    def __init__(self, model, color, storage, price, os_version):
        super().__init__(model, color, storage, price, os_version)

