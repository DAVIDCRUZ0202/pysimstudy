import numpy as np

def clipVec(ids, seq, event):
    """
    Takes three vectors of a dataframe. Loops through the ids vector
    And uses the sequence vector to keep track of position
    When certain events are met through the event vector,
    the function stores a resulting count of id's to keep which is returned
    """

    last = []
    maxperiod = max(seq)
    xid = 0
    seqtrunc = 0

    for i in range(len(ids)):
        if event[i] == 0:
            xid += 1
        if event[i] == 1:
            if seqtrunc == 0:
                xid += 1
                last.append(xid)
                xid = 0
                seqtrunc += 1
        if seq[i] == maxperiod:
            if seqtrunc == 0:
                last.append(xid)
                xid = 0
            else:
                seqtrunc = 0
    return last

# Rcpp::IntegerVector matMultinom(Rcpp::NumericMatrix probmatrix) {

#   int rows = probmatrix.nrow();

#   Rcpp::IntegerVector ans(rows);

#   for(int i = 0; i < rows; ++i) {
#     ans[i] = vecMultinom(probmatrix(i, _));
#   }

#   return(ans);
# }

def matMultinom(probmatrix: np.matrix):
    """

    Args:
        probmatrix (_type_): _description_
    """
    rows = len(probmatrix)

    ans = np.zeros(rows)

    for i in range(rows):
        ans[i] = vecMultinom(probmatrix[i])

    print(ans)
    return ans


def vecMultinom(probs):
    """_summary_

    Args:
        probs (_type_): _description_
    """
    import numpy as np

    # print(probs[0])

    k = len(probs)
    # ans = np.zeros(k)
    ans = np.random.multinomial(n=1, size=k, pvals=np.array(probs[0])[0])

    # we are making assumption that ans is equal to rmultinom output

    total = 0

    for i in range(k):
        total += ans[0][i] * (i+1)
    
    return total

# int vecMultinom(NumericVector probs) {

#   int k = probs.size();

#   IntegerVector ans(k);
#   rmultinom(1, probs.begin(), k, ans.begin());

#   int total = 0;

#   for(int i = 0; i < k; ++i) {
#     total += ans[i] * (i + 1);
#   }

#   return(total);
# }