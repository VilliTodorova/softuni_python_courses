from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[str] = []
        self.workers: List[str] = []

    def add_animal(self, animal: str, price: float) -> str:
        if price <= self.__budget and self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity - len(self.workers) > 0:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0

        for worker in self.workers:
            salaries += worker.salary

        if self.__budget - salaries >= 0:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending = 0

        for animal in self.animals:
            tending += animal.money_for_care

        if self.__budget - tending >= 0:
            self.__budget -= tending
            return f"You tended all the ex_05_animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the ex_05_animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                lions.append(animal)
            elif type(animal).__name__ == "Tiger":
                tigers.append(animal)
            elif type(animal).__name__ == "Cheetah":
                cheetahs.append(animal)

        lions_info = '\n'.join(str(lion) for lion in lions)
        tigers_info = '\n'.join(str(tiger) for tiger in tigers)
        cheetahs_info = '\n'.join(str(cheetah) for cheetah in cheetahs)

        return f"You have {len(self.animals)} ex_05_animals\n----- {len(lions)} " \
               f"Lions:\n{lions_info}\n----- {len(tigers)} Tigers:\n" \
               f"{tigers_info}\n----- {len(cheetahs)} Cheetahs:\n{cheetahs_info}"

    def workers_status(self) -> str:
        caretakers = []
        keepers = []
        vets = []

        for worker in self.workers:
            if type(worker).__name__ == "Caretaker":
                caretakers.append(worker)
            elif type(worker).__name__ == "Keeper":
                keepers.append(worker)
            elif type(worker).__name__ == "Vet":
                vets.append(worker)

        caretakers_info = '\n'.join(str(caretaker) for caretaker in caretakers)
        keepers_info = '\n'.join(str(keeper) for keeper in keepers)
        vets_info = '\n'.join(str(vet) for vet in vets)

        return f"You have {len(self.workers)} workers\n----- {len(keepers)} " \
               f"Keepers:\n{keepers_info}\n----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_info}\n----- {len(vets)} Vets:\n{vets_info}"