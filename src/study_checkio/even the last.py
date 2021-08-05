def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    try:
        for i in array[::2]:
            print(i)
            sum += i
        sum = sum * array[-1]
        print(sum)
    except:
        return 0

array = [0, 1, 2, 3, 4, 5]
checkio(array)