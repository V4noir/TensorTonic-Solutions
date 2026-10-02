import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    if not seqs:
        return np.empty((0, 0), dtype=int)
    final=[]
    if max_len is None:
        max_len=0
        for row in seqs:
            b=len(row)
            if(max_len<b):
                max_len=b
    for row in seqs:
        newRow = list(row[:max_len])
        while len(newRow)<max_len:
            newRow.append(pad_value)
        final.append(newRow)
    return np.asarray(final,dtype=int)