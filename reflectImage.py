#this function reflects a 2d image on the initial basis vector given a non orthonagal basis vectors 
# firstly it orthonormalize the basis using Gram-Schmidt method then it uses the follwing transformations to get the reflected vectors in the my orthonormal basis
#    R(orthonormal basis)       R reflected in the orthonormal basis
 #   |                             |
#    | E inverse                   | E 
#    |               TE            |
#    R(New basis) --------- R(new basis) reflected 
import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
from readonly.bearNecessities import *
import GramSchmidt
def build_reflection_matrix(newBasis) : 
    E = GramSchmidt.gsBasis(newBasis)
    # Write a matrix in component form that performs the mirror's reflection in the mirror's basis.
    # Recall, the mirror operates by negating the last component of a vector.
    # Replace a,b,c,d with appropriate values
    TE = np.array([[1, 0],
                   [0, -1]])
    # Combine the matrices E and TE to produce your transformation matrix.
    T = inv(E) @ TE @ E
    # Finally, we return the result. There is no need to change this line.
    return T
