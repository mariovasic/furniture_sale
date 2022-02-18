import pytest
from decimal import Decimal
from datetime import date
from dummy import calculate_discount


_test_data_valids = [
    pytest.param(date(2022, 12, 24), Decimal('0.01'), Decimal('0.15')),
    pytest.param(date(2022, 1, 1), Decimal('0.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('0.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('0.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('0.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('0.01'), Decimal('0.05')),
    pytest.param(date(2022, 12, 23), Decimal('0.01'), Decimal('0.05')),
    pytest.param(date(2022, 11, 26), Decimal('0.01'), Decimal('0.15')),
    pytest.param(date(2022, 1, 1), Decimal('99.99'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('99.99'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('99.99'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('99.99'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('99.99'), Decimal('0.05')),
    pytest.param(date(2022, 12, 23), Decimal('99.99'), Decimal('0.05')),
    pytest.param(date(2022, 11, 26), Decimal('99.99'), Decimal('0.15')),
    pytest.param(date(2022, 12, 24), Decimal('99.99'), Decimal('0.15')),
    pytest.param(date(2022, 1, 1), Decimal('100.00'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('100.00'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('100.00'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('100.00'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('100.00'), Decimal('0.1')),
    pytest.param(date(2022, 12, 23), Decimal('100.00'), Decimal('0.1')),
    pytest.param(date(2022, 11, 26), Decimal('100.00'), Decimal('0.19')),
    pytest.param(date(2022, 12, 24), Decimal('100.00'), Decimal('0.19')),
    pytest.param(date(2022, 1, 1), Decimal('100.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('100.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('100.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('100.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('100.01'), Decimal('0.1')),
    pytest.param(date(2022, 12, 23), Decimal('100.01'), Decimal('0.1')),
    pytest.param(date(2022, 11, 26), Decimal('100.01'), Decimal('0.19')),
    pytest.param(date(2022, 12, 24), Decimal('100.01'), Decimal('0.19')),
    pytest.param(date(2022, 1, 1), Decimal('499.99'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('499.99'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('499.99'), Decimal('0.00')),
    pytest.param(date(2022, 1, 1), Decimal('499.99'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('499.99'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('499.99'), Decimal('0.1')),
    pytest.param(date(2022, 12, 23), Decimal('499.99'), Decimal('0.1')),
    pytest.param(date(2022, 11, 26), Decimal('499.99'), Decimal('0.19')),
    pytest.param(date(2022, 12, 24), Decimal('499.99'), Decimal('0.19')),
    pytest.param(date(2022, 1, 1), Decimal('500.00'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('500.00'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('500.00'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('500.00'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('500.00'), Decimal('0.2')),
    pytest.param(date(2022, 12, 23), Decimal('500.00'), Decimal('0.2')),
    pytest.param(date(2022, 11, 26), Decimal('500.00'), Decimal('0.28')),
    pytest.param(date(2022, 12, 24), Decimal('500.00'), Decimal('0.28')),
    pytest.param(date(2022, 1, 1), Decimal('500.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 25), Decimal('500.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 27), Decimal('500.01'), Decimal('0.00')),
    pytest.param(date(2022, 12, 31), Decimal('500.01'), Decimal('0.00')),
    pytest.param(date(2022, 11, 28), Decimal('500.01'), Decimal('0.2')),
    pytest.param(date(2022, 12, 23), Decimal('500.01'), Decimal('0.2')),
    pytest.param(date(2022, 11, 26), Decimal('500.01'), Decimal('0.28')),
    pytest.param(date(2022, 12, 24), Decimal('500.01'), Decimal('0.28')),

]

@pytest.mark.parametrize("day, total, expected ", _test_data_valids)
def test_sale(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # assert
    assert actual == expected


_test_data_invalid_input = [
    pytest.param( date( 2022,12,24 ), "Mario", id = "57" ),
    pytest.param( date( 2022,12,24 ), Decimal( "0.00" ), id = "58" ),
    pytest.param( date( 2022,12,24 ), Decimal( "-0.01" ), id = "59" ),
    pytest.param( date( 2022,12,24 ), Decimal( "-5000.00" ), id = "60" ),
    pytest.param( "Mario", Decimal( "5.00" ), id = "61" ),
    pytest.param( date( 2022,11,27 ), Decimal( "50.00" ), id = "62" ),
    pytest.param( date( 2022,12,26 ), Decimal( "500.00" ), id = "63" )]

@pytest.mark.parametrize( "total,day", _test_data_invalid_input )
def test_invalid_input( total: Decimal, day: date ):
    with pytest.raises( ValueError ):
        calculate_discount( total, day )


