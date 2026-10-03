def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    recommended=set(recommended[:k])
    relevant=set(relevant)
    r=len(recommended & relevant)
    return [r/k,r/len(relevant)]
    
    
    