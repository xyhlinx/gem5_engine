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
            print('\'{:s}\': MyO3Processor({}, {}, {}, \'{}\'),'.format(name, *a))

    def res(self, base_parameters, picking):
        self.ans = []
        self.base_parameters = base_parameters
        picking = [(i, picking[i]) for i in range(len(picking))]
        for i in range(0, len(picking) + 1):
            path = []
            self.backtracking(picking, 0, i, path)
        self.custom_print(self.ans)

    def backtracking(self, picking, idx, nums, path):
        if len(path) == nums:
            tmp_ans = []
            pos = 0
            for i in range(len(self.base_parameters)):
                if pos >= nums or path[pos][0] > i:
                    tmp_ans.append(self.base_parameters[i])
                    continue
                tmp_ans.append(path[pos][1])
                pos += 1

            self.ans.append(tmp_ans)
            return

        for i in range(idx, len(picking)):
            path.append(picking[i])
            self.backtracking(picking, i + 1, nums, path)
            path.pop()


if __name__ == '__main__':
    base_parameters = [2, 16, 48, 'simple']
    picking = [8, 192, 256, 'complex']

    s = Solution()
    s.res(base_parameters, picking)
    