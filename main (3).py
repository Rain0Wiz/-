# Ассоциация - наследование при котором один класс является полем другого класса(Целое состоит из частей)
# ассоциация-АГРЕГАЦИЯ - в UML (Унифицированный язык моделирования) - линия с незакрашенным ромбом(часть удалена объект-целое остаётся)
class Salary:
    def __init__(self, pay):
        self.pay = pay # оплата за месяц
    # метод вывода зарплаты за год
    @property
    def getSummOfYear(self):
        return int(self.pay*12)

class Worker:
    def __init__(self, pay, bonus, name):
        self.pay = pay
        self.bonus = bonus
        self.name = name

    # метод - выводит зарплату сотрудника за год вместе с примией
    def getSummOfYearForWorker(self):
        return f"Зарплата за год вместе с примией у сотрудника {self.name} состовляет {self.bonus + self.pay.getSummOfYear}"

# объект - зарплата за месяц
salary_of_month = Salary(20000)
print(salary_of_month.getSummOfYear)
# объект - работник
sasha = Worker(salary_of_month, 20000, "Саша")
print(sasha.getSummOfYearForWorker())
        
            
                    