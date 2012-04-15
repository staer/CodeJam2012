#!/usr/bin/python

def generate_recycled_numbers(n):
    """ Given a number, find all of it's 'recycled' variants """
    n = str(n)
    results = []
    letters = list(n)[1:]
    while letters:
        n = "%s%s" % (letters.pop(), n[0:-1])
        results.append(int(n,10))
    
    return results


def fast_recycled(t):
    """ Given t = (A, B) - go through all versions of n between A and B and determine all unique pairs """
    A = t[0]
    B = t[1]
    count = 0

    unique_pairs = set()
    for n in xrange(A, B):
        recycled = generate_recycled_numbers(n)
        for m in recycled:
            if m  > n and m <= B:       # the number is in the appropriate range!
                unique_pairs.add((n, m))

    return len(unique_pairs)    


if __name__ == "__main__":
    """ 
    First line of stdin contains the number of test cases. 
    Each line of input contains 2 numbers A, B where A <= n < m <= B
    Out put should be 'Case #X: <recycled_count>'
    """
    import sys
    f = sys.stdin

    T = int(f.readline())

    from multiprocessing import Pool, cpu_count
    pool = Pool(processes=cpu_count())

    # For each test case to follow
    inputs = []
    for i in xrange(T):
        A, B = f.readline().split(' ')
        A = int(A)
        B = int(B)
        inputs.append((A, B))
    
    # Do some multiprocessing magic just cause we can
    results = pool.map(fast_recycled, inputs)

    for i, r in enumerate(results):
        print "Case #%s: %s" % ((i+1), r)

