#!/usr/bin/python3
"""
ボード初期化
プレイヤー１初期化
プレイヤー２初期化
ボート表示
プレイヤー１入力受付
ボード更新
勝敗判定
プレイヤー２入力受付
ボード更新
勝敗判定
"""
from getch import getch,pause
from copy import deepcopy
import os
p1 = "p1"
p2 = "p2"
winner = ""
board = [[" "," "," "] for x in range(3)]
players = [p1,p2]
playerMark = ["X","O"]
nowPlayer = 0
pointer = [0,0]
masks = [
    [
        [
            ["X"," "," "],
            ["X"," "," "],
            ["X"," "," "]
        ],
        [
            ["X","X","X"],
            [" "," "," "],
            [" "," "," "]
        ],
        [
            ["X"," "," "],
            [" ","X"," "],
            [" "," ","X"]
        ],
        [
            [" "," ","X"],
            [" ","X"," "],
            ["X"," "," "]
        ]
    ],
    [
        [
            ["O"," "," "],
            ["O"," "," "],
            ["O"," "," "]
        ],
        [
            ["O","O","O"],
            [" "," "," "],
            [" "," "," "]
        ],
        [
            ["O"," "," "],
            [" ","O"," "],
            [" "," ","O"]
        ],
        [
            [" "," ","O"],
            [" ","O"," "],
            ["O"," "," "]
        ]
    ]
]
def printBoard(board,pointer=None):
    boardBorder = " {} | {} | {} \n"
    boardBorder+= "---|---|---\n"
    boardBorder+= " {} | {} | {} \n"
    boardBorder+= "---|---|---\n"
    boardBorder+= " {} | {} | {} \n"
    boardCopy = deepcopy(board)
    if pointer != None:
        boardCopy[pointer[0]][pointer[1]] = "@"
    print(boardBorder.format(boardCopy[0][0],boardCopy[0][1],boardCopy[0][2],boardCopy[1][0],boardCopy[1][1],boardCopy[1][2],boardCopy[2][0],boardCopy[2][1],boardCopy[2][2]))
#print(printBoard(board,pointer))
from getch import getch, pause
print(players[nowPlayer] + "さんのターンです。")
printBoard(board,pointer)
print(len(masks[nowPlayer]))
while winner == "":
    key = ord(getch())
    os.system("clear")
    print(key)
    if key == 3:
        break
    elif key == 27:
        key = ord(getch())
        if key == 91:
            key = ord(getch())
            if key == 65:
                #print("↑")
                pointer[0] -= 1
                pointer[0] = abs(pointer[0]%3)
            elif key == 66:
                #print("↓")
                pointer[0] += 1
                pointer[0] = abs(pointer[0]%3)
            elif key == 67:
                #print("→")
                pointer[1] += 1
                pointer[1] = abs(pointer[1]%3)
            elif key == 68:
                #print("←")
                pointer[1] -= 1
                pointer[1] = abs(pointer[1]%3)
        else:
            print("無効な入力")
    elif key == 13:
        board[pointer[0]][pointer[1]] = playerMark[nowPlayer]
        #勝敗判定
        #ボードから抽出する
        tmpBoard = [["@","@","@"] for i in range(len(board))]
        for m in masks[nowPlayer]:
            for i in range(len(m)):
                for j in range(len(m[i])):
                    if board[i][j] == m[i][j]:
                        tmpBoard[i][j] = board[i][j]
                    else:
                        tmpBoard[i][j] = " "
            #printBoard(tmpBoard)
            if tmpBoard == m:
                winner = players[nowPlayer]
                print(winner + "さんの勝ちです。")
        #プレイヤー交換
        if nowPlayer == 0: nowPlayer = 1
        else: nowPlayer = 0
    if winner == "":
        print(players[nowPlayer] + "さんのターンです。")
        printBoard(board,pointer)
printBoard(board)
print("終了")