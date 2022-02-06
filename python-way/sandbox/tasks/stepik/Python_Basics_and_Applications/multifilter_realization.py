"""
task link -> https://stepik.org/lesson/24464/step/4?unit=6769
"""

class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterator = iter(iterable)
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return self

    def __next__(self):
        try: 
            el = next(self.iterator)
        except:
            raise StopIteration
    
        pos, neg = 0, 0
        for func in self.funcs:
            if func(el):
                pos += 1
            else:
                neg += 1

        if self.judge(pos, neg):
            return el
        else:
            el = self.__next__()
            return el


if __name__ == '__main__':
    def mul2(x):
        return x % 2 == 0

    def mul3(x):
        return x % 3 == 0

    def mul5(x):
        return x % 5 == 0


    a = [i for i in range(31)] # [0, 1, 2, ... , 30]

    print(list(multifilter(a, mul2, mul3, mul5))) 
    # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

    print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
    # [0, 6, 10, 12, 15, 18, 20, 24, 30]

    print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
    # [0, 30]