x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

def new_func():
    global x

print(x)
escopo()
print(x)