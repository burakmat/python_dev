abc = {"a": 1, "b": 2, "c": 3}
cba = {}
for k in abc:
    d = abc["{}".format(k)]
    cba[d] = k

# province_premier
# premier_province

print(cba)
print(type(abc))


print(len(abc))
print(abc)