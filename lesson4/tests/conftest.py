import pytest
from lesson4.app.services.payment_service import BankAcount, BankOffice


@pytest.fixture
def new_bank_acount()-> BankAcount:
    return BankAcount(owner_name="Leonard")


@pytest.fixture
def bank_acounts_for_office() ->list[BankAcount]:
    return [
        BankAcount(owner_name="Leonard"),
        BankAcount(owner_name="Tankred"),
        BankAcount(owner_name="Cristina"),
    ]
    


@pytest.fixture
def bank_office_with_account(
    bank_acounts_for_office: list[BankAcount]) ->BankOffice:
    b = BankOffice()
    
    for account in bank_acounts_for_office:
        b.add_account(account=account)
        
    return b