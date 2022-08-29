from functools import reduce
import numpy as np


def find_array_in_array(ar, ar2):

    # Find all matches with first element of ar2
    slices = tuple(slice(None, -s + 1) for s in ar2.shape)
    match_idx = np.nonzero(ar[slices] == ar2.flat[0])
    
    # ar[:-ar2.shape[0]:, :-ar2.shape[1]]

    # Check remaining indices of ar2
    for idx in list(np.ndindex(ar2.shape))[1:]:

        if len(match_idx[0]) == 0:
            break

        # Index into ar offset by idx
        nz2 = tuple(m + i for m, i in zip(match_idx, idx))

        # Find remaining matches with selected element
        to_keep = np.nonzero(ar[nz2] == ar2[idx])[0]
        match_idx = tuple(m[to_keep] for m in match_idx)

    return match_idx