from lesson4.app.services.payment_service import BankAcount, BankOffice
import pytest


def test_bank_account_case_ok():
    b = BankAcount(owner_name="Leonard")
    b.increase_by(100)
    b.decrease_by(50)
    
    assert b.account_sum() == 50.0


def test_bank_account_fixture_case_ok(
    new_bank_acount:BankAcount,
):
    new_bank_acount.increase_by(100)
    new_bank_acount.decrease_by(50)
    
    assert new_bank_acount.owner_name() == "Leonard"
    assert new_bank_acount.account_sum() == 50.0


def test_bank_office_case_raise_exception(
    new_bank_acount:BankAcount,
    bank_office_with_account:BankOffice
    ) -> None:
    with pytest.raises(ValueError) as ex:
        bank_office_with_account.add_account(new_bank_acount)
        
    assert ex.value.args[0] == "Owner already present"