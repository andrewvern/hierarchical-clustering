from hierarchical_cluster import HierachicalCluster
from binary_heap import BinaryHeap
from pair import Pair
import numpy as np
import pandas as pd


def main():
    df = pd.read_csv(r'cancer.csv', header=None)
    df_size = len(df.values)
    df_list = []
    for i in range(df_size):
        df_sample = toList(df, i)
        df_list.append(df_sample)

    hc_list = []
    for samp in df_list:
        hc = HierachicalCluster(samp[0], samp[1:])
        hc_list.append(hc)
       
    while len(hc_list) > 1:
        bmh = BinaryHeap()
        pairs_list = all_pairs(hc_list)
        for pair in pairs_list:
            bmh.insert(pair)

        min = bmh.del_min()
        new_cluster = HierachicalCluster('branch', None, distance=min.compute_distance())            
        new_cluster.set_left_child(min.get_hc_member1())
        new_cluster.set_right_child(min.get_hc_member2())
        new_cluster.compute_centroid()
        hc_list.append(new_cluster)
        hc_list.remove(new_cluster.get_left_child())
        hc_list.remove(new_cluster.get_right_child())
        print(len(hc_list))

    leaves = hc_list[0].get_all_leaves()
    roots = []
    for i in range(len(leaves)):
        roots.append(leaves[i].get_root())
    df = pd.DataFrame(data=roots)
    hc_list[0].print()
    print('hi')

def toList(df, ri):
    a = df.loc[ri]
    b = a.to_numpy()
    c = b.tolist()
    return c

def all_pairs(hc_list):
    pairs = []
    for i in range(len(hc_list)-1):
        for j in range(i+1,len(hc_list)):
            pair = Pair(hc_list[i],hc_list[j])
            pairs.append(pair)
    return pairs

main()