from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan_obj = self._create_new_loan(loan_type)
        self.loans.append(loan_obj)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client_obj = self._create_new_client(client_type, client_name, client_id, income)
        self.clients.append(client_obj)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client_obj = self._find_client_by_id(client_id)
        loan_obj = self._find_loans_by_type(loan_type)[0]

        if loan_type != client_obj.CLIENT_TYPE:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan_obj)
        client_obj.loans.append(loan_obj)

        return f"Successfully granted {loan_type} to {client_obj.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client_obj = self._find_client_by_id(client_id)

        if client_obj is None:
            raise Exception("No such client!")

        if client_obj.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_obj)
        return f"Successfully removed {client_obj.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans = self._find_loans_by_type(loan_type)
        [loan.increase_interest_rate() for loan in loans]

        return f"Successfully changed {len(loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                counter += 1
                client.increase_clients_interest()

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_income = sum(c.income for c in self.clients)
        granted_loans = sum(len(client.loans) for client in self.clients)
        amount_granted_loans = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        amount_not_granted_loans = sum(loan.amount for loan in self.loans)
        avg_interest = sum(client.interest for client in self.clients) / len(self.clients) if self.clients else 0

        return f"Active Clients: {len(self.clients)}\nTotal Income: {total_income:.2f}\n" \
               f"Granted Loans: {granted_loans}, Total Sum: {amount_granted_loans:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {amount_not_granted_loans:.2f}\n" \
               f"Average Client Interest Rate: {avg_interest:.2f}"

    # helper methods

    def _find_client_by_id(self, client_id):
        client = [client for client in self.clients if client.client_id == client_id]
        return client[0] if client else None

    def _find_loans_by_type(self, loan_type):
        return [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]

    def _find_clients_by_interest_rate(self, min_rate):
        return [client for client in self.clients if client.interest < min_rate]

    def _create_new_client(self, client_type, client_name, client_id, income):
        return self.CLIENT_TYPES[client_type](client_name, client_id, income)

    def _create_new_loan(self, loan_type):
        return self.LOAN_TYPES[loan_type]()
