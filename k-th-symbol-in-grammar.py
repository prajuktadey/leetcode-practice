class Solution:
    def kthGrammar(self, n, k):
        are_values_same = True

        n = 2**(n - 1)

        while n != 1:
            # Halve the number of elements in the row.
            n //= 2

            # If k is in the second half of the row, adjust k and toggle the flag.
            if k > n:
                k -= n
                are_values_same = not are_values_same

        
        return 0 if are_values_same else 1
