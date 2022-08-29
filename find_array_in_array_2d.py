import numpy as np


def find_array_in_array_2d(ar, ar2):

    # Find all matches with first element of ar2
    match_idx = np.nonzero(ar == ar2[0, 0])

    # Check remaining indices of ar2
    for i, j in list(np.ndindex(ar2.shape))[1:]:

        if len(match_idx[0]) == 0:
            break

        # Index into ar offset by i, j
        nz2 = [match_idx[0] + i, match_idx[1] + j]

        # Remove any that are out of bounds
        not_oob = (nz2[0] < ar.shape[0]) & (nz2[1] < ar.shape[1])
        nz2 = nz2[0][not_oob], nz2[1][not_oob]

        # Find remaining matches with selected element
        to_keep = np.nonzero(ar[nz2] == ar2[i, j])[0]
        match_idx = match_idx[0][to_keep], match_idx[1][to_keep]

    return match_idx