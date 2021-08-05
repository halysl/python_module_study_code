def checkio(*args):
    try:
        i = list(args)
        max_num = max(i)
        min_num = min(i)
        chaju = max_num - min_num
        return (chaju)
    except:
        return 0

checkio(1,2,13)