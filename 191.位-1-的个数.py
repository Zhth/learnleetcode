import time
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """     
def print_run_time(func):  
    def wrapper(*args, **kw):  
        local_time = time.time()  
        func(*args, **kw) 
        print('current Function [%s] run time is %.2f' % (func.__name__ ,time.time() - local_time))  
    return wrapper 

# @print_run_time    
def getBitnum1(n):
    start = time.clock()
# #long running
# #do something other
# end = time.clock()
    temp = 0
    while n > 0:
        temp += n & 1
        n >>= 1
    end = time.clock()
    print(temp)
    print((end - start) * 10e10)
    return temp

def getBitnum2(n):
    start = time.clock()
# #long running
# #do something other
# end = time.clock()
    temp = 0
    while n > 0:
        n &= (n - 1)
        temp += 1
    end = time.clock()
    print(temp)
    print((end - start) * 10e10)
    return temp

def getresult(n):
    print('method1:')
    getBitnum1(n)
    print('method2:')
    getBitnum2(n)

getresult(98949453135454867351356465443165487975435131654897365423)
# for i in range(10):
#     n = n >> 1
#     print(n)