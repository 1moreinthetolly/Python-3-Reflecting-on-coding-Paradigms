# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

nested_arrays = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
print(flatten_and_sort(nested_arrays))

'''
How does this solution ensure data immutability?
    *This solution ensures data immutability because it doesn't modify the original input.

Is this solution a pure function? Why or why not?
    *Yes, this solution is a pure function. It consistently produces the same output for the same input, and it doesn't have any side effects.

Is this solution a higher order function? Why or why not?
    *No, this solution is not a higher-order function. This function only takes a list as input and doesn't involve passing or returning functions.

Would it have been easier to solve this problem using a different programming style?
    *Given the straightfoward style of the solution, others methods may become more complex/less readable.

Why in particular is functional programming a helpful paradigm when solving this problem?
    *Functional programming emphasizes immutability, pure functions, and avoiding side effects.
'''