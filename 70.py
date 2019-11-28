# class Solution:
#     def climbStairs(self, n: int) -> int:

#         def com(n, m):
#             if m > n//2:
#                 m = n - m
#             result = 1
#             for i in range(m):
#                 result *= (n - i)
#             for i in range(m - 1):
#                 result = result //(i + 2)
#             return result

#         if n <= 1:
#             return 1
#         n += 1
#         result = 0
#         if n % 2:
#             for i in range(n//2 + 1):
#                 result += com(n, 2*i + 1) * 5**i
#             return result//2**(n - 1)
#         elif n % 4:
#             for i in range(n//4):
#                 result += com(n, 2*i + 1) * (5**i + 5**(n//2 - 1 - i))
#             result += com(n, n//2) * 5**((n//2 - 1)//2)
#             return result//2**(n - 1)
#         else:
#             for i in range(n//4):
#                 result += com(n, 2*i + 1) * (5**i + 5**(n//2 - 1 - i))
#             return result//2**(n - 1)
def fibo3(n):
    '''序列解包'''
    a, b = 1, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return a