from program import app

def test_func():
    assert app.func(4) == 8
    assert app.func(5) == 10
    assert app.func(20) == 40
    assert app.func(1.5) == 3

