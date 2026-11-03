from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_subtract():
    assert subtract(6, 2) == 4
    
def test_multiply():
    assert multiply(6, 2) == 12

def test_divide_uneven():
    assert divide(7, 2) == 3.5

