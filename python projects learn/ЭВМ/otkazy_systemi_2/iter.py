import copy

from typing import List, Tuple

from matrix import Matrix
from bucket import Bucket, BucketIndexer

import numpy as np


matrixTest = [[0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 0, 1, 0],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 0, 1, 0]]

bucketsTest = [[0, 1],
               [2, 3, 4],
               [5, 6, 7]]


def do_iter(
    mtx: Matrix,
    bucket_indexer: BucketIndexer,
) -> None:
    for bucket in bucket_indexer.buckets:
        end = False
        
        while not end:
            excepted = except_bucket_nodes(mtx.n, bucket)

            b_nodes = [None] * bucket.len
            r = np.ndarray((bucket.len, len(excepted)))
            for b_node_idx, b_node in enumerate(bucket.nodes):
                b_nodes[b_node_idx] = b_node
                for e_node_idx, e_node in enumerate(excepted):
                    other_b_idx = bucket_indexer.n2b(e_node)

                    sum1 = len(bucket.nodes & mtx.crosses(e_node))
                    sum2 = len(bucket.nodes & mtx.crosses(b_node))
                    sum3 = len(bucket_indexer.at(other_b_idx).nodes & mtx.crosses(b_node))
                    sum4 = len(bucket_indexer.at(other_b_idx).nodes & mtx.crosses(e_node))

                    r[b_node_idx, e_node_idx] = (sum1 - sum2) + (sum3 - sum4) - 2 * mtx.mtx[b_node][e_node]

            max_idx = np.unravel_index(r.argmax(), r.shape)
            max_val = r[max_idx[0]][max_idx[1]]

            real_vertex_1 = b_nodes[max_idx[0]]
            real_vertex_2 = excepted[max_idx[1]]

            if max_val > 0:
                bucket_indexer.swap_nodes(real_vertex_1, real_vertex_2)
                # mtx.swap_nodes(max_idx[0], max_idx[1])
            else:
                end = True

def except_bucket_nodes(
    n: int, 
    bucket: Bucket,
) -> List[int]:
    ret = [None] * (n - bucket.len)
    cnt = 0

    # TODO : с 0 или с 1 ?
    for i in range(0, n):
        if i not in bucket.nodes:
            ret[cnt] = i
            cnt += 1

    return ret

def swap_point(
    mtx: Matrix,
    x: int,
    y: int,
) -> None:
    # second_column = list()
    # first_column = list()

    # for i in mtx.mtx:
    #     second_column.append(i[y - 1])
    #     first_column.append(i[x - 1])

    # count_i = 0
    # for i in mtx.mtx:
    #     count_i += 1
    #     i[y - 1] = first_column[count_i - 1]
    #     i[x - 1] = second_column[count_i - 1]

    # second_line = mtx.mtx[y - 1]
    # first_line = mtx.mtx[x - 1]

    # mtx.mtx[y - 1] = first_line
    # mtx.mtx[x - 1] = second_line

    mtx.swap_cols(x, y)
    mtx.swap_rows(x, y)
