class Solution:
    def seq(self, n):
        if n<=1:
            return n
        return self.seq(n-1)+self.seq(n-2)

    def fib(self, n: int) -> int:

        return self.seq(n)

if __name__ == "__main__":
    n= int(input())
    sol= Solution()
    print(sol.fib(n))
