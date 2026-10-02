import numpy as np

def entropy_node(y: list[int]) -> float:
    if y is None or len(y)==0:
        return float(0)
    else:
        y=np.asarray(y)
        a,values=np.unique(y,return_counts=True)
        allValues=np.sum(values)
        probs=[]
        for value in values:
            probs.append(value/allValues)
        probs=np.asarray(probs)
        H=-np.sum(probs*np.log2(probs))
        return float(H)