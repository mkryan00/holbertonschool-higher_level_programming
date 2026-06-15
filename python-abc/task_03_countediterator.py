#!/usr/bin/python3
"""Module that defines the CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        """Initializes CountedIterator with an iterable and a counter.
        Args:
        iterable: Any iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items iterated so far.
        Returns:
        int: The current count of iterated items.
        """
        return self.count

    def __next__(self):
        """Fetches the next item and increments the counter.
        Returns:
        The next item from the iterator.
        Raises:
        StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        # Raises StopIteration naturally when exhausted
        self.count += 1
        return item

    def __iter__(self):
        """Returns the iterator object itself.
        Returns:
        CountedIterator: The iterator itself.
        """
        return self
