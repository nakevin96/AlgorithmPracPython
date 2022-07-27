class A:
    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        return super().__new__()
    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)

def how_works():
    x = A(1, 2, 3, x= 4)

    # x = A.__new__(A, *args, **kwargs)
    # if isinstance(x, A):
    #     type(x).__init__(x, *args, **kwargs)

def main():
    how_works()

if __name__ == '__main__':
    pass