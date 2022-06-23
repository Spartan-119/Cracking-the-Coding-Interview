def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1s1 = s1 + s1
        if s2 in s1s1:
            return True
        else:
            return False


# calling the driver function
if __name__ == '__main__':
    print(isRotation('Abin', 'nAbi'))
