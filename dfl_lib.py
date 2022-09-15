from typing import List, Tuple

def conv_2_tuple(lst):
    return tuple(lst)

def conv_2_list(lst):
    if not hasattr(lst, '__iter__'):
        return (lst, None)
    elif isinstance(lst, List) or isinstance(lst, Tuple):
        def helper(cur_tup, cur_id):
            nonlocal lst
            if cur_id == -1:
                return cur_tup
            return helper(tuple((lst[cur_id], cur_tup)), cur_id - 1)
        return helper(tuple((lst[len(lst) - 1]), None), len(lst) - 2)
    else:
        raise NotImplementedError