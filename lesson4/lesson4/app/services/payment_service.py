
class BankAcount:
    _sum:float = 0.0
    _owner_name: str = ""
    
    def __init__(self, owner_name:str)-> None:
        self._owner_name = owner_name
    
    def increase_by(self, sum:float)-> float:
        self._sum +=sum
        return self._sum
    
    def decrease_by(self, sum:float)-> float:
        self._sum -=sum

    def owner_name(self) ->str:
        return self._owner_name

    def account_sum(self) ->float:
        return self._sum
    
    
class BankOffice:
    _accounts: list[BankAcount] = []
    
    def __init__(self):
        pass
    
    def add_account(self, account:BankAcount)-> None:
        if account.owner_name() in [x.owner_name() for x in self._accounts]:
            raise ValueError("Owner already present")
        
        self._accounts.append(account)
    
    def list_positive_accounts(self):
        return {x.owner_name():x.account_sum() for x in self._accounts if x.account_sum() > 0}
    
    def list_non_positive_accounts(self):
        return {x.owner_name():x.account_sum() for x in self._accounts if x.account_sum() <= 0}
