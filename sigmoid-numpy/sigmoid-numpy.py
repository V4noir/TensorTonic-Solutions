import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    xDizi = np.asarray(x)
    xDizi = 1/(1+np.exp(-xDizi))

    return xDizi