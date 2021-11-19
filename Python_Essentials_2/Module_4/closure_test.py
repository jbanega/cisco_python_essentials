def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


closure_1 = make_closure(2)
closure_2 = make_closure(3)

for i in range(5):
    print(i, closure_1(i), closure_2(i))