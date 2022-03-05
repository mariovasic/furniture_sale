import pytest
from decimal import Decimal
from dummy import calculate_price



_test_data_ = [
    pytest.param(int('1'), bool(False), Decimal("2"), id="1"),
    pytest.param(int('2'), bool(False), Decimal("2"), id="2"),
    pytest.param(int('4'), bool(False), Decimal("2"), id="3"),
    pytest.param(int('5'), bool(False), Decimal("3"), id="4"),
    pytest.param(int('7'), bool(False), Decimal("3"), id="5"),
    pytest.param(int('9'), bool(False), Decimal("3"), id="6"),
    pytest.param(int('10'), bool(False), Decimal("4"), id="7"),
    pytest.param(int('13'), bool(False), Decimal("4"), id="8"),
    pytest.param(int('17'), bool(False), Decimal("4"), id="9"),
    pytest.param(int('18'), bool(False), Decimal("5"), id="10"),
    pytest.param(int('65'), bool(False), Decimal("5"), id="11"),
    pytest.param(int('66'), bool(False), Decimal("3"), id="12"),
    pytest.param(int('100'), bool(False), Decimal("3"), id="13"),
    pytest.param(int('200'), bool(False), Decimal("3"), id="14"),

    pytest.param(int('1'), bool(True), Decimal("1.8"), id="15"),
    pytest.param(int('2'), bool(True), Decimal("1.8"), id="16"),
    pytest.param(int('4'), bool(True), Decimal("1.8"), id="17"),
    pytest.param(int('5'), bool(True), Decimal("2.7"), id="18"),
    pytest.param(int('7'), bool(True), Decimal("2.7"), id="19"),
    pytest.param(int('9'), bool(True), Decimal("2.7"), id="20"),
    pytest.param(int('10'), bool(True), Decimal("3.6"), id="21"),
    pytest.param(int('13'), bool(True), Decimal("3.6"), id="22"),
    pytest.param(int('17'), bool(True), Decimal("3.6"), id="23"),
    pytest.param(int('18'), bool(True), Decimal("4.5"), id="24"),
    pytest.param(int('65'), bool(True), Decimal("4.5"), id="25"),
    pytest.param(int('66'), bool(True), Decimal("2.7"), id="26"),
    pytest.param(int('100'), bool(True), Decimal("2.7"), id="27"),
    pytest.param(int('200'), bool(True), Decimal("2.7"), id="28"),
    pytest.param(int('22'), bool(True), Decimal("4.5"), id="29"),
    pytest.param(int('22'), bool(False), Decimal("5"), id="30")
]


@pytest.mark.parametrize('age, group, expected', _test_data_)
def test_price_(age: int, group: bool, expected: Decimal):
    # Act
    actual = calculate_price(age, group)
    # assert
    assert actual == expected


_test_data_invalid=[
    pytest.param(int('2'), 'x', id ="31" ),
    pytest.param("XX", bool(True), id ="32" ),
    pytest.param(int(0), bool(True), id="33")

]


@pytest.mark.parametrize( "age, group", _test_data_invalid)
def test_price_invalid( age: int, group: bool):
    with pytest.raises( ValueError ):
     calculate_price( age, group )

    with pytest.raises(ValueError) as exception_info:
        calculate_price(age, group)
    assert exception_info.type == ValueError