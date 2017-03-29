def test():
    r=2
    r=yield r
    yield r
    print(4)


t=test()
print(t.__next__())
print(t.send(3))


