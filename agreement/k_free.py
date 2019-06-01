from __future__ import division

# Author: Raynor Vliegendhart
# LICENSE: MIT
 
def multirater_kfree(n_ij, n, k):
    '''
    Computes Randolph's free marginal multirater cohen_kappa for assessing the 
    reliability of agreement between annotators.
    
    Args:
        n_ij: An N x k array of ratings, where n_ij[i][j] annotators 
              assigned case i to category j.
        n:    Number of raters.
        k:    Number of categories.
    Returns:
        Percentage of overall agreement and free-marginal cohen_kappa
    
    See also:
        http://justusrandolph.net/cohen_kappa/
    '''
    N = len(n_ij)
    
    P_e = 1./k
    P_O = (
        1./(N*n*(n-1))
        * 
        (sum(n_ij[i][j]**2 for i in xrange(N) for j in xrange(k)) - N*n)
    )
    
    kfree = (P_O - P_e)/(1 - P_e)
    
    return P_O, kfree
 

example1 = dict(
n = 3,
k = 2,
n_ij = [
    [3, 0],
    [2, 1],
    [1, 2],
    [0, 3]
]
)
 
example2 = dict(
 n = 3,
 k = 2,
 n_ij = [
   [3, 0],
   [2, 1],
   [1, 2],
   [3, 0]
 ]
)
 

def test():
    print multirater_kfree(**example1)  #  P_O = 0.667, kfree = 0.333
    print multirater_kfree(**example2)  #  P_O = 0.667, kfree = 0.333

if __name__ == "__main__":
    print test()  #  P_O = 0.667, kfree = 0.333
    #print multirater_kfree(example2)  #  P_O = 0.667, kfree = 0.333
