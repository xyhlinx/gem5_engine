class Memoization(object):

    def __init__(self):
        self.cache = {1: 9999}

    def __call__(self, func):
        def wrapper(cls, nums):
            if nums in self.cache:
                return self.cache[nums]
            res = func(cls, nums)
            self.cache[nums] = res
            return res

        return wrapper


class Solution:

    def custom_print(self, ar):
        for a in ar:
            name = map(lambda x: str(x), a)
            name = '_'.join(name)
            print('{:s}'.format(name))

        for a in ar:
            name = map(lambda x: str(x), a)
            name = '_'.join(name)
            print('{:s}: MyO3Processor({}, {}, {}, \'{}\'),'.format(name, *a))

    def res(self, origin, picking):
        self.ans = []
        self.origin = origin
        for i in range(2, 5):
            path = []
            self.backtracking(picking, 0, i, path)
        self.custom_print(self.ans)

    def backtracking(self, picking, idx, nums, path):
        if len(path) == nums:
            tmp_ans = []
            pos = 0
            for i in range(len(self.origin)):
                if pos >= nums or path[pos][0] > i:
                    tmp_ans.append(self.origin[i])
                    continue
                tmp_ans.append(path[pos][1])
                pos += 1

            self.ans.append(tmp_ans)
            return

        stack = []
        for i in range(idx, len(picking)):
            path.append(picking[i])
            self.backtracking(picking, i + 1, nums, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    origin = [2, 16, 48, 'simple']
    picking = [(0, 8), (1, 192), (2, 256), (3, 'complex')]
    s.res(origin, picking)
    