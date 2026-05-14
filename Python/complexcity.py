"""Find the biggest number in a list with clear, line-by-line comments.

Time complexity: O(n) — we scan the list once.
Space complexity: O(1) — only a single extra variable used.
"""

def find_biggest_number(sample_array):
        # Line 1: Assume the first element is the biggest so far. (O(1))
        biggest_number = sample_array[0]

        # Line 2: Iterate over the array starting from index 1 to the end. (O(n))
        for index in range(1, len(sample_array)):
                # Line 3: Compare the current element with the biggest seen so far. (O(1))
                if sample_array[index] > biggest_number:
                        # Line 4: Update the biggest number when we find a larger element. (O(1))
                        biggest_number = sample_array[index]

        # Line 5: After scanning all elements, print the biggest number. (O(1))
        print("Biggest number:", biggest_number)


if __name__ == "__main__":
        # Example usage and simple test data
        sample_array = [5, 7, 9, 2, 3, 4]
        find_biggest_number(sample_array)

# calculete total time complexity: O(n) + O(1) + O(1) + O(1) + O(1) = O(n)