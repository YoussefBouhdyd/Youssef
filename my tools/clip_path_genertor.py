def clip_path(N:int) -> str:
    """
    This function help us in creating clip path for creating the form of fork in the
    background of some sections
    N : number of fork that you want to creat
    """
    path = "clip-path: polygon(0 0,"
    patern = 100 / N
    X = 0
    Y = 0
    while(X < 100):
        X += patern
        if Y:
            Y = 0
        else:
            Y = "var(--fork-hight)"
        path += f"{X:.2f}% {Y},"
    path += "100% 100%,0% 100%)"
    return path

print(clip_path(80))