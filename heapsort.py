"""
Heap Sort Algorithm Implementation
This script sorts an array using the Heap Sort algorithm.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify a subtree rooted at index i.

    :param arr: List of integers representing the heap.
    :param n: Size of the heap.
    :param i: Index of the root node.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    """
    Sorts an array using the Heap Sort algorithm.

    :param arr: List of integers to be sorted.
    """
    n = len(arr)

    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    # Example usage
    numbers = [12, 11, 13, 5, 6, 7]
    heap_sort(numbers)
    print("Sorted array is:", numbers)
