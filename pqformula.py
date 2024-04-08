def quad_equation(p, q):
    """Function for second order pq-formula"""
    import math

    disc = p*p/4 - q
    if disc >= 0:
        d = math.sqrt(disc)
        x1 = (-p/2 + d)
        x2 = (-p/2 - d)
        return x1, x2
    else:
        d = math.sqrt(-disc)
        x1 = complex(-p/2, d)
        x2 = complex(-p/2, d)
        return x1, x2