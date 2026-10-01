import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:

    weights=np.zeros(X.shape[1])
    bias=0.0
    for i in range(steps):
        
        p=_sigmoid(X@weights+bias)
        
        loss=-np.mean((y*np.log(p)+(1-y)*np.log(1-p)))
        dw=X.T@(p-y)/len(y)
        db=np.mean(p-y)
        weights=weights-lr*dw
        bias=bias-lr*db
    return weights, bias
        