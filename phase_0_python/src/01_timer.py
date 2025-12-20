# Implement a @timer decorator and apply it to 3 different functions (data load, train, evaluate).

from datetime import datetime

def timer(f):
    def inner():
        start  = datetime.now()
        result = f()
        end = datetime.now()
        print(end - start)
        return result
    return inner


def load_data():
    return None

def train():
    return None

def evaluate():
    return None


# o = timer(load_data)
# t = timer(train)
# e = timer(evaluate)


# print(o(),t(),e())