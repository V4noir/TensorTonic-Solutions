import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    x=np.asarray(x)
    p=np.asarray(p)
    sonuc=np.sum(x*p)
    return float(sonuc)