from pqformula import quad_equation

def test_quad_equation():
    assert quad_equation(2, 1) == (-1, -1)
    assert quad_equation(4, 5) == ((-2 + 1j), (-2 + 1j))
    assert quad_equation(-6, 5) == (5, 1)
