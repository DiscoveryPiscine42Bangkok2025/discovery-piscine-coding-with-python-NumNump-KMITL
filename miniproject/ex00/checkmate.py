def checkmate(board):
    try:
        # Clean board
        rows = board.strip().split("\n")
        size = len(rows)
        
        # Check board is square
        if any(len(row) != size for row in rows):
            print("Error (Board isn't Square)")
            return
        
        # Use find_king for get king position
        king_pos = find_king(rows)
        if king_pos is None  :
            print("Error (Can't find King)")
            return

        #Check that can king check
        if (
            check_pawn(rows,king_pos) or
            check_rook(rows,king_pos) or
            check_bishop(rows,king_pos) or
            check_queen(rows,king_pos)
        ):
            print("Success")
        
        else :
            print("Fail (Can't Checkmate)")
        

        
    
    except Exception:
        print("Error")

#Find King position
def find_king( rows ) :
    king_pos = None
    size = len(rows)
    
    for i in range(size) :
        for j in range(size) :
            if rows[i][j].upper() == "K" :
                if king_pos is not None :
                    return None
                king_pos = (i,j)
    
    return king_pos
    
def check_line(rows,king_pos,directions,valid) :
    #ตรวจจับการเดินใช้กับตัวที่เดินเป็นเส้น
    size = len(rows)
    xk , yk = king_pos
    for dx , dy in directions :
        x , y = xk + dx , yk + dy  #เช็ครอบตัว king
        while 0 <= x < size and 0 <= y < size : #เช็คว่ายังอยู่ในกระดาน
            piece = rows[x][y]
            if piece != "." and piece != "K" :
                if piece in valid :
                    return True
                break
            x += dx #บวกไปเรื่อยๆจนกว่าจะเจอ
            y += dy
    
    return False


def check_pawn(rows,king_pos) :
    x , y = king_pos
    size = len(rows)

    # กินเฉียง
    if x < size - 1 and y > 0 and rows[x+1][y-1] == "P" :
        return True
    if x < size - 1 and y < size - 1 and rows[x+1][y+1] == "P" :
        return True

    return False

def check_rook(rows,king_pos) :
    #เดินเป็นรูป +
    return check_line(rows,
        king_pos,
        directions=[(-1,0),(1,0),(0,-1),(0,1)],
        valid={"R"}
        )


def check_bishop(rows,king_pos) :
    #เดินเป็นรูป x
    return check_line(
        rows,
        king_pos,
        directions=[(-1,-1),(-1,1),(1,-1),(1,1)],
        valid={"B"}
        )


def check_queen(rows,king_pos) :
    #เดินเป็นแมงมุม (rook + bishop)
    return check_line(
        rows,
        king_pos,
        directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)],
        valid= {"Q"}
    )
