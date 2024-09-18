# Um modulo deve ser capaz de ser extendido, mas nunca alterado

class Company:
    def do_work(self, worker: int) -> None:
        if worker == 1:
            print('Programmer creating code...')
        elif worker == 2:
            print('Seller selling the product')
        elif worker == 3:
            print('Human Resources hiring devs')
        else:
            print('Error, no worker!')

            