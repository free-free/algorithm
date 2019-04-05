import copy


class Node(object):

    def __init__(self, val=None):
        self.val = val
        self.next = None



def reverse_link_table1(hd):
    if hd == None or hd.next == None:
        return hd
    pre = hd
    nxt = hd.next
    while nxt.next!= None:
        tmp = nxt.next
        nxt.next = pre
        pre = nxt
        nxt = tmp
    nxt.next = pre
    hd.next = None
    return nxt


def reverse_link_table2(hd):
    cur = None
    while hd is not None:
        tmp = hd.next
        hd.next = cur
        cur = hd
        hd = tmp
    return cur


def create_link_table(vals):
    hd = Node(vals[0])
    cur = hd
    for val in vals[1:]:
        cur.next =  Node(val)
        cur = cur.next
    return hd


def print_link_table(hd):
    vals = []
    while hd != None:
        vals.append(hd.val)
        hd = hd.next
    print(vals)

def check_palindrome(hd):
    is_palindrome = True
    step = 0
    fast_ptr = hd
    slow_ptr = hd
    # use fast and slow pointer to find the central pointer of link table
    while fast_ptr and fast_ptr.next :
        step += 1
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    left_hd = hd
    # reverse right-side link table and return head pointer
    right_hd = reverse_link_table2(slow_ptr)
    # save right-side link table head pointer
    right_tmp = right_hd
    # check is a palindrome link table
    for i in range(step):
        if right_hd.val != left_hd.val:
            is_palindrome = False
            break
        right_hd = right_hd.next
        left_hd = left_hd.next
    # reverse right-side link table to what it originally looks like
    tmp_ptr = None
    right_ptr = right_tmp
    while tmp_ptr != slow_ptr:
        nxt = right_ptr.next
        right_ptr.next = tmp_ptr
        tmp_ptr = right_ptr
        right_ptr = nxt
    return is_palindrome
    

def find_link_table_middle_point(hd):
    fast_ptr = hd
    slow_ptr = hd
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr

        

hd = create_link_table('maed')
print_link_table(hd)
hd = reverse_link_table1(hd)
print_link_table(hd)
hd = reverse_link_table2(hd)
print_link_table(hd)
print(check_palindrome(hd))
print_link_table(hd)
mid_ptr = find_link_table_middle_point(hd)
print(mid_ptr.val)
