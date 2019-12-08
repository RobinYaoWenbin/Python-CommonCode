# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:49:28 2019

@author: wenbin
"""

"""
LRU是least recently used的缩写,它的意思是"最近最少使用",LRU缓存就是使用这种原理实现,
简单的说就是缓存一定量的数据,当超过设定的阈值时就把一些过期的数据删除掉.常用于页面置换算法,是虚拟页式存储管理中最常用的算法.
如何实现LRU缓存方案.
"""

from collections import deque

def InsertURL(que , page):
    # insert page to the queue.
    try:
        ind = que.index(page)
    except Exception as e:
        que.append(page)
    else:
        que.remove(page)
        que.append(page)
    finally:
        print("{0} has been inserted successfully!".format(page))


def LRUImplement(k):
    # implement the LRU plan.
    # The parameter is k, after the size of the queue supass the k, then delete the supassing part.
    # 初始化队列。
    queue = deque(maxlen = k)  # new a queue to store the data
    queue.append(1) # 将page1加入到queue中去
    queue.append(3) ; queue.append(4) ; queue.append(7)
    print(queue)
    # insert a URL that has already in the queue
    InsertURL(queue , 4)
    print(queue)
    # insert a URL that is not in the queue yet.
    InsertURL(queue , 5)
    print(queue)


if __name__ == "__main__":
    LRUImplement(3)