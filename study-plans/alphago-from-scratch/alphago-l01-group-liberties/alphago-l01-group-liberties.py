import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    board= np.asarray(board)
    queue=[]
    queue.append((row,col))
    liberties=set()
    x,y=board.shape
    visited=set()
    target=board[row,col]
    while queue:
        cRow,cCol=queue.pop(0)
        visited.add((cRow,cCol))
        if cRow-1>=0:
            if board[cRow-1,cCol]==0:
                liberties.add((cRow-1,cCol))
            elif board[cRow-1,cCol]==target and (cRow-1,cCol) not in visited:
                queue.append((cRow-1,cCol))
                visited.add((cRow-1, cCol))
        if cRow+1<x:
            if board[cRow+1,cCol]==0:
                liberties.add((cRow+1,cCol))
            elif board[cRow+1,cCol]==target and (cRow+1,cCol) not in visited:
                queue.append((cRow+1,cCol))
                visited.add((cRow+1, cCol))
        if cCol-1>=0:
            if board[cRow,cCol-1]==0:
                liberties.add((cRow,cCol-1))
            elif board[cRow,cCol-1]==target and (cRow,cCol-1) not in visited:
                queue.append((cRow,cCol-1))
                visited.add((cRow, cCol-1))
        if cCol+1<y:
            if board[cRow,cCol+1]==0:
                liberties.add((cRow,cCol+1))
            elif board[cRow,cCol+1]==target and (cRow,cCol+1) not in visited:
                queue.append((cRow,cCol+1))
                visited.add((cRow, cCol+1))
    group = sorted([list(pos) for pos in visited])
    libs = sorted([list(pos) for pos in liberties])
    
    return (group, libs)