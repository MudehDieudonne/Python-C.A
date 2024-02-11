def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can 
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first. 
    Does not modify the list. 
    Returns the sum of the longest run. 
    """
    if len(L) < 2:
        return sum(L)

    longest_run = [0, 1]
    current_run = [0, 1]
    increasing = True

    for i in range(1, len(L)):
        if (L[i] > L[i-1] and increasing) or (L[i] < L[i-1] and not increasing):
            current_run[1] = i
        else:
            if current_run[1] - current_run[0] > longest_run[1] - longest_run[0]:
                longest_run = current_run[:]
            current_run = [i, i+1]
        increasing = L[i] > L[i-1]

    if current_run[1] - current_run[0] > longest_run[1] - longest_run[0]:
        longest_run = current_run

    return sum(L[longest_run[0]:longest_run[1]])

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
longest_run_sum = longest_run(L)
print(f"The longest monotonical run in L is {longest_run_sum}.")
