def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
    return []

def generate_subsets(nums):
    res = []
    def backtrack(i, curr):
        if i == len(nums):
            res.append(list(curr))
            return
        curr.append(nums[i])
        backtrack(i + 1, curr)
        curr.pop()
        backtrack(i + 1, curr)
    backtrack(0, [])
    return res

if __name__ == "__main__":
    print("Fibonacci(6):", fibonacci(6))
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Subsets:", generate_subsets([1, 2]))
