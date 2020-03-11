# Ada Bishop 2


t = int(input())
chessBoard = [[0 for j in range(8)] for i in range(8)]


def getNextMovePos(sr, sc, chessBoard, totalCovered):

    # if(chessBoard[sr][sc] != 1):

    pass


def tryPath(sr, sc, chessBoard, totalCovered, paths, blockedtl, blockedtr, blockedbl, blockedbr):
    if(totalCovered == 64):
        # print the paths
        return
    chessBoard[sr][sc] = 1
    for i in range(8):
        # try top-left
        if(sr-i >= 0 and sc-i >= 0 and (not blockedtl)):
            paths.append((sr-i, sc-i))
            tryPath(sr-i, sc-i, chessBoard, totalCovered+1, paths, 1, 0, 0, 1)

    nextRow, nextCol = getNextMovePos(sr, sc, chessBoard, totalCovered)


while(t):
    sr, sc = [int(x) for x in input().split()]
    print(sr, sc, chessBoard)
    paths = []
    tryPath(sr, sc, chessBoard, 0, paths, 0, 0, 0, 0)

    t -= 1
