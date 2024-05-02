from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0
    PRICE_INCREMENT = 1.1
    EQUIPMENT_TYPE = "ElbowPad"

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.PRICE_INCREMENT
