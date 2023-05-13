def play(n, sourse, receiver, storage):
    """
    The function of moving n disks in the Tower of Hanoi puzzle.
    Function arguments:
    The first argument n is an integer, the number of disks in the pyramid.
    source, receiver, storage - any type.
    The second argument is sourse, the rod from which we shift the disks.
    The third argument is the receiver, the rod on which we shift the disks.
    The fourth argument is storage, the pivot on which we shift n-1 disks
    for temporary storage in the process of general work.
    """
    assert n > -1, "Number of disks 'n' must be greater -1"
    if n <= 0:
        return
    play(n-1, sourse, storage, receiver)
    print("Диск ", n, " : ", sourse, " --> ", receiver)
    play(n-1, storage, receiver, sourse)


play(10, 'a', 'b', 'c')
