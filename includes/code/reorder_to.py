def reorder_to(A, B):
    """Return order of rows in A the best match rows in B."""
    distance_matrix = np.ones((6, 6))*np.inf
    for i, a in enumerate(A):
        for ii, b in enumerate(B):
            ba = (b-a)
            distance_matrix[i, ii] = np.sqrt(np.dot(ba, ba))
            
    reorder = [[] for _ in range(6)]
    for _ in range(6):
        ind = np.argmin(distance_matrix)
        i, ii = ind/6, ind%6
        reorder[ii] = i
        distance_matrix[i, :] = np.inf
        distance_matrix[:, ii] = np.inf
    
    return reorder