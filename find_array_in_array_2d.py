import numpy as np


def find_array_in_array_2d(ar, ar2):

    # Find all matches with first element of ar2
    match_idx = np.nonzero(ar[:-ar2.shape[0]+1, :-ar2.shape[1]+1] == ar2[0, 0])

    # Check remaining indices of ar2
    for i, j in list(np.ndindex(ar2.shape))[1:]:

        # End if no possible matches left
        if len(match_idx[0]) == 0:
            break

        # Index into ar offset by i, j
        nz2 = (match_idx[0] + i, match_idx[1] + j)

        # Find remaining matches with selected element
        to_keep = np.nonzero(ar[nz2] == ar2[i, j])[0]
        match_idx = match_idx[0][to_keep], match_idx[1][to_keep]

    return match_idx