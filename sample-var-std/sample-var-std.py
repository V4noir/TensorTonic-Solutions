import numpy as np

def sample_var_std(x: list) -> dict:
    x=np.asarray(x)
    l=len(x)
    mean=np.sum(x)/l
    uv=1/(l-1)*np.sum((x-mean)**2)
    deviation=uv**0.5
    return {
        "variance": float(uv),
        "standard_deviation": float(deviation)
    }