"""


"""

List2 = [[10,20,30,40],
        [50,60,70,80],
        [90,100,110,120]]

def lsp(a):
    c = 0
    L2 = len(a[c]) - 1
    NewList = []
    while 0 <= c and c <= L2:
        L1 = len(a) - 1
        mymax = 0
        r = 0
        while 0 <= r and r <= L1:
            mymax = mymax + a[r][c]
            r = r + 1
        
        c = c + 1
        NewList.append(mymax)
    return NewList
    
print lsp(List2)


List2 = [[10,20,30,40],
         [50,60,70,80],
         [90,100,110,120]]
## this is code that can sum each row in a 2D List
def lsp2(a):
    r = 0
    L1 = len(a) - 1
    NewList = []
    while 0 <= r and r <= L1:
        mysum = 0
        c = 0
        L2 = len(a[r]) - 1
        while 0 <= c and c <= L2:
            mysum = mysum + a[r][c]
            c = c + 1
        NewList.append(mysum)
        r = r + 1
    return NewList

print lsp2(List2)
print

## you had trouble with column summing
#the solution is:
# if you can sum the rows then you should be able to sum
#the columns if you write the code mostly in backwards
def lsp3(a):
    c = 0
    L2 = len(a) - 1
    NewList = []
    while 0 <= c and c <= L2:
        mysum = 0
        r = 0
        L1 = len(a[c]) - 1
        while 0 <= r and r <= L1:
            mysum = mysum + a[r][c]
            r = r + 1
        NewList.append(mysum)
        c = c + 1
    return NewList

print lsp3(List2)
print


















































    
