

def move_the_line():
    x1 = 1
    x2 = 1
    x3 = 1


    w1 = 3
    w2 = 4
    b = -10
    lr = 0.1

    result = float("-inf")
    i = 0
    print("iteration " + str(i) + ": " + str(result))


    while result < 0 and i < 20:
        
       
        
        w1 += x1 * lr
        w2 += x2 * lr
        b += x3 * lr
        i += 1
        result = (line(x1, x2, w1, w2, b))
        print("iteration " + str(i) + ": " + str(result))
        print("x1: " + str(x1) + ", w1: " + str(w1) + ", x2: " + str(x2) + ", w2: " + str(w2) + ", b: " + str(b))
        print()
        

def line(x1, x2, w1, w2, b):
    return( (w1 * x1) + (w2 * x2) + b )


if __name__ == '__main__':
    move_the_line()
