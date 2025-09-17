import sys
from checkmate import checkmate, print_board

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        try:
            with open(filename) as f:
                board = f.read()
            
            #แสดงboard
            print_board(board)
            
            #เช็คว่า King โดนเซ็ทหย่อมั้ย
            checkmate(board)

            print()
        except:
            print("Error")
            print()
