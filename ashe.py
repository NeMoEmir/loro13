class WashingMachine:
    def init(self):
        self.powder = 1000
        self.conditioner = 1000

    def __subtract_powder(self, powder):
        return self.powder - powder
    
    def __subtract_conditioner(self, conditioner):
        return self.conditioner - conditioner

    def wash_clothes(self, powder, conditioner):
        if self.conditioner >= conditioner and self.powder >= powder:
            self.__subtract_conditioner(conditioner)
            self.__subtract_powder(powder)
            print('Процесс стирки завершен!.')
            print(f'осталось {self.conditioner-conditioner} мл кондиционера и {self.powder - powder}  гр порошка')
        else:
            if self.conditioner < conditioner:
                print(f'вам не хватает {conditioner - self.conditioner} мл кондиционера')
            if self.powder < powder:
                print(f'вам не хватает {powder - self.powder}  гр порошка')


beko = WashingMachine()
p = int(input('введите количество требуемого порошка: '))
c = int(input('введите количество требуемого кондиционера: '))
beko.wash_clothes(p, c)