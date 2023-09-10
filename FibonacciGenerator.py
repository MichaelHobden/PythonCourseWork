def fibGenerator(num):
    num1 = 0;
    num2 = 1;
    for i in range(20):
        temp = num1
        num1 = num2
        num2 += temp
        yield temp
for item in fibGenerator(20):
    print(item)
