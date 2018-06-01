import datetime


class BankCreditRequest(object):

    def __init__(self, name, surname, birth_date, salary, credit_amount,
                 credit_term):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.salary = salary
        self.credit_amount = credit_amount
        self.credit_term = credit_term

    def age_check(self):
        return datetime.datetime.now().year - self.birth_date >= 18

    def credit_check(self):
        if self.age_check():
            if self.credit_amount / (self.credit_term * 12) * 1.09 \
                    < self.salary * 0.7:
                response = "Credit for %s %s approved." % (self.name,
                                                           self.surname)
            else:
                response = "Credit for %s %s rejected due to insolvency." % \
                           (self.name, self.surname)
        else:
            response = "Credit for %s %s rejected due to the fact that the " \
                       "client is not of legal age." % \
                       (self.name, self.surname)
        return response

    def print_information(self):
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Birth date: ", self.birth_date)
        print("Salary: ", self.salary)
        print("Credit amount: ", self.credit_amount)
        print("Credit term: ", self.credit_term)
        print("Bank's response to credit request: ", self.credit_check())


client1 = BankCreditRequest('John', 'Trace', 1975, 1000, 6000, 1)
client1.print_information()
print()
client1 = BankCreditRequest('Kate', 'Smith', 2001, 500, 3000, 2)
client1.print_information()
print()
client1 = BankCreditRequest('Ben', 'Nevis', 1990, 900, 19000, 2)
client1.print_information()
