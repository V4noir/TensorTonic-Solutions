def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    for i in range(steps) :
        gradient= ((2*a*x0)+b)
        x0=x0-(lr*gradient)
        
    return x0