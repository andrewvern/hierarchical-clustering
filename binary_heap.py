class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.size = 0
        
    def __str__(self):
        return str(self.heap_list)
    
    def __len__(self):
        return self.size
    
    def __contains__(self, item):
        return item in self.heap_list
    
    def is_empty(self):
        return self.size == 0
    
    def find_min(self):
        if self.size > 0:
            min_val = self.heap_list[1]
            return min_val
        return None
        
    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)
        
    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size = self.size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def min_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
            
    def build_heap(self, alist):
        index = len(alist) // 2 # any nodes past the half way point are leaves
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percolate_down(index)
            index -= 1
        
    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2
            
    def percolate_down(self, index):
        while (index * 2) <= self.size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc
