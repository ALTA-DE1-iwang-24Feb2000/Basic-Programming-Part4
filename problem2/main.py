def draw_xyz(N):
    pattern = ""
    angka = 1
    for i in range(1, N+1 ):
        for j in range (1, N+1 ):
            if angka %3 == 0:
               pattern += 'X' + " "
            elif angka %2 == 0 :
                pattern += 'Z' + " "
            else:
                pattern += 'Y' + " "
            angka += 1
        pattern += '\n'

    if angka > N:
        angka = 1
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """