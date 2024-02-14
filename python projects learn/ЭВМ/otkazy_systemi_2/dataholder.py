from typing import List
from collections import deque

from bucket import Bucket, BucketIndexer
from metrics import Metrics
from matrix import Matrix, StreamMatrix

class DataHolder:
    def __init__(self, filename: str) -> None:
        self._buckets_sizes: List[int] = []
        self._buckets: List[Bucket] = [] 
        self._mtx: Matrix = None

        self._load_file_metrics: Metrics = Metrics()
        self._forward_metrics: Metrics = Metrics()

        self._load_file_metrics.spent.start()

        with open(filename, 'r') as f:
            if not f.readable():
                raise 'unknown format: the first line not readble'

            line = f.readline()
            if line is None or line == '':
                raise 'unknown format: the first line is empty'

            self._buckets_sizes = list(map(int, line.split(' ')))
            if not f.readable():
                raise 'unknown format: the second is not readble'
            # self._buckets.sort(reverse=True)

            self._load_file_metrics.total_ops_cnt.add(len(self._buckets_sizes))

            self._mtx = StreamMatrix(stream=f)
            
        self._load_file_metrics.spent.observe()

    def get_bucket_sizes(self) -> List[int]:
        return self._buckets_sizes

    def get_mtx(self) -> Matrix:
        return self._mtx

    def forward(self, buckets_p: List[int]) -> BucketIndexer:
        mtx = self._mtx
        buckets: List[Bucket] = []
        for i, px in enumerate(buckets_p):
            buckets.extend([Bucket(self._buckets_sizes[i], mtx.mtx) for _ in range(px)])
        
        self._forward_metrics.total_ops_cnt.add(len(buckets))

        node_q = deque([mtx.degrees.index(min(mtx.degrees))])
        node_q.extend([x for x in range(mtx.n)])

        self._forward_metrics.total_ops_cnt.add(len(mtx.degrees))

        bucket_idx = 0
        visited = [False] * mtx.n

        while len(node_q) > 0 and bucket_idx < len(buckets):
            i = node_q.popleft()
            self._forward_metrics.total_ops_cnt.incr()
            if visited[i]:
                continue

            # visited[i] = True

            crosses = [] 
            for x in mtx.crosses(i):
                if not visited[x]:
                    crosses.append(x)
            
            bad_nodes = buckets[bucket_idx].add(*list(crosses))
            for x in buckets[bucket_idx].nodes:
                visited[x] = True
            
            for node in bad_nodes:
                # visited[node] = False
                node_q.append(node)

            if buckets[bucket_idx].full:
                bucket_idx += 1

        return BucketIndexer(mtx, buckets)
