import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m=np.asarray(m)
    v=np.asarray(v)
    grad=np.asarray(grad)
    param=np.asarray(param)
    mOld=0
    vOld=0
    m=(beta1*m)+(1-beta1)*grad
    mOld=m
    v=(beta2*v)+(1-beta2)*grad**2
    vOld=v
    m=m/(1-beta1**t)
    v=v/(1-beta2**t)
    param=param-(lr*m/(v**0.5+eps))
    return (param,mOld,vOld)
    