A, B = map(int, input().split())

def add(A, B):
    result = A + B
    return result

def div(A, B):
    try:
        result = A / B
        return result
    except ZeroDivisionError:
        result = A

def  mul():
    result = A * B
    return result

def sub():
    result = A - B
    return result



