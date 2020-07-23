#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Zachary Gerber, Michael DeMory, Tiffany Mclean'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value
        return

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.key == other.key
        else:
            return NotImplemented


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = [[] for _ in range(num_buckets)]
        self.num = num_buckets

    def __repr__(self):
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        node_a = Node(key, value)

        index_bucket = self.buckets[node_a.hash % self.num]

        for i in index_bucket:
            if i == node_a:
                index_bucket.remove(i)
                break
        index_bucket.append(node_a)

    def get(self, key):
        find_node = Node(key)

        index_bucket = self.buckets[find_node.hash % self.num]

        for i in index_bucket:
            if i == find_node:
                return i.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)
