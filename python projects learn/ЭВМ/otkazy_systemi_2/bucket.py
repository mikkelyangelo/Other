from typing import Iterable, List, Set, Dict

from matrix import Matrix

class Bucket(object):
    def __init__(self, size: int, mtx: List[List], nodes: List[int]=[]) -> None:
        self._mtx = mtx
        self._size = size
        self._nodes = set(nodes)

    @property
    def max_size(self) -> int: return self._size

    @property
    def len(self) -> int: return len(self._nodes)

    @property
    def full(self) -> bool: return len(self._nodes) == self._size

    @property
    def nodes(self) -> Set[int]: return self._nodes

    def set_size(self, size: int):
        self._size = size

    def extend_links(self, node_idx: int) -> int:
        ret = 0
        for i, x in enumerate(self._mtx[node_idx]):
            if i not in self._nodes:
                ret += x
        return x

    def remove(self, *nodex_idxs: List[int]) -> None:
        for node in nodex_idxs:
            self.nodes.remove(node)

    def add(self, *node_idxs: List[int]) -> List:
        if len(self._nodes) + len(node_idxs) <= self.max_size:
            for node_idx in node_idxs:
                self._nodes.add(node_idx)
            return []
        
        ex_links = []
        for node in self._nodes:
            ex_links_cnt = self.extend_links(node)
            ex_links.append((node, ex_links_cnt))
        for node in node_idxs:
            ex_links_cnt = self.extend_links(node)
            ex_links.append((node, ex_links_cnt))
        ex_links.sort(key=lambda x: x[1])

        self._nodes = set([ x[0] for x in ex_links[:self._size] ])
        return [ x[0] for x in ex_links[self._size:] ]

    def swap(self, other) -> None:
        self.nodes, other.nodes = other.nodes, self.nodes

class BucketIndexer(object):
    def __init__(self, mtx: Matrix, buckets: Iterable[Bucket]) -> None:
        self._mtx: Matrix = mtx
        self._buckets: List[Bucket] = list(buckets)
        
        self._n: int = mtx.n
        # index for storing bucket id per node
        self._n2b: Dict[int, int] = {}
        
        for i, bucket in enumerate(self._buckets):
            self._n2b.update({x: i for x in bucket.nodes})

    @property
    def buckets(self) -> List[Bucket]: return self._buckets 

    @property
    def score(self) -> int:
        ret = 0
        for bucket in self._buckets:
            ret += sum([bucket.extend_links(node) for node in bucket.nodes])/2
        return ret

    def at(self, i: int) -> Bucket: return self._buckets[i]

    def n2b(self, x: int) -> int: return self._n2b[x]

    def swap_nodes(self, x: int, y: int) -> None:
        x_b, y_b = self._buckets[self._n2b[x]], self._buckets[self._n2b[y]]
        x_b.remove(x)
        x_b.add(y)
        y_b.remove(y)
        y_b.add(x)
        self._n2b[x], self._n2b[y] = self._n2b[x], self._n2b[y]
