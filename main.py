import math, queue 
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
      left = p.get()
      right = p.get()
      p.put(TreeNode(left,right,(left.data[0]+right.data[0], "")))
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}): 
    # TODO - perform a tree traversal and collect encodings for leaves in code
    if ((node.left == None)and(node.right==None))#if both are empty
      code[node.data[1]] == prefix#set the prefix
    if (node.left != None):#left node exists
      get_code(node.left,prefix+"0",code)#grab its code aka prefix and add 0
    if (node.right != None)
      get_code(node.right,prefix+"1",code)#grab and add 1
    return (code)#get the code we just found/made
  #length of this encoding is its cost
      

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):#cost of char is its depth on the tree. each leaf is a char
    # TODO
    #cost of every char *  num char
  #ceiling for round up lg of how many bits we have (how many bits per that num of chars)
  #return(len(get_code(f))) #i tried
  bits = math.ceil(math.log2(len(f.keys())))
  cost = 0#initalize
  for i in f.keys():
    cost += sum(bits * f[i])
  return cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f): #right cost means tree was right
    # TODO
    #num of char * cost of char. len string * cost of char
  #simple loop. for every val in frequency sum bits for that char times frequency
  cost = 0 #init
  for i in f.keys():
    cost += len(C[i] * f[i])
  return cost

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))