Google Code Jam 2012
====================

These are my entries for the Google Code Jam 2012 contest. I decided to fool around with this at the last minute and probably won't make it past the first round. That being said here are my solutions to whatever problems I attempt to solve.

All of these solutions were developed in Python 2.7.2 and executed in [Pypy 1.8](http://pypy.org). This is actually my first time using pypy, so I decided to benchmark number crunching run times between pypy and CPython. I thought that runtime would be an issue since the competition limits runtime to 4 minutes on a small input and 8 minutes on large. Benchmark results are below.

For more information about the Google Code Jam see the contest website at: [http://code.google.com/codejam](http://code.google.com/codejam). My entries are submitted under the contestant name "Staer".


## Qualification Round ##

### A. Speaking in Tongues ###

Built the translation matrix from the sample input that was provided. Sample data provided contained all letter mappings except for 'z' which was easy to determine by process of elimination. The rest of the program just switches the content of the input using the translation matrix.

**Run time in pypy (only input): 0.04 seconds**

Run time in CPython (only input): 0.02 seconds 

### B. Dancing with the Googlers ###

For each score, find the best possible score (either standard or surprising) by looking at every combination of 3-judge scores possible in reverse order. Once an appropriate score is found return it. Once each Googlers best 'standard' and 'surprisng' scores have been found, simply go though them in order and increment a counter if the highest number in their score is greater than the threshold. Check the 'standard' score first, then 'surprisng' if we haven't already used up our number of surprising scores, otherwise don't incrememt the counter. The solution is the final counter value.

**Run time in pypy (large input): 0.16 seconds**

Run time in CPython (large input): 0.51 seconds

### C. Recycled Numbers ###

Start with n=A and iterate to n=B-1. For any given 'n', find out all the possible "recycled" numbers that it can be turned into. For example "1234" can be recycled into "4123", "3412", and "2341". Check each of these numbers to make sure that it is 1.) Greater than 'n' (definition of the problem) and 2.) Less than or equal to B (definition of problem). If the 'recycled' number fits these criteria add them to a set (sets can't have duplicates). When iteration is complete, the length of the set is the solution.

Note: I first tried a brute force approach which worke for the small input but didn't scale well at all.

**Run time in pypy (large input): 14.9 seconds**

Run time in CPython (large input): 48.6 seconds

### D. Hall of Mirrors ###

Did not participate


