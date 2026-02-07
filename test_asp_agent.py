import os
import sys
from asp_agent import ASPAgent

# Mock board state (5x9)
# 0: empty, 1: black, 2: white
def create_mock_board():
    board = [[0 for _ in range(9)] for _ in range(5)]
    # Set up a simple capture scenario for White (2) moving to capture Black (1)
    # White at (2, 2)
    # Black at (2, 3)
    # White moves (2,2) -> (2,1) (withdrawal capture?)
    # Or White moves (2,2) -> (2,3) (approach capture?) - illegal if occupied
    
    # Let's simple scenario:
    # W at 2,2
    # B at 2,3
    # W moves 2,2 -> 2,1 (withdrawal away from 2,3 capture?) 
    # Wait, withdrawal captures piece BEHIND start. 
    # If W moves 2,2 -> 2,1, withdrawal direction is (1,0) (East). 
    # Piece at 2,3 (Start + Dir) is captured.
    
    board[2][2] = 2 # White
    board[2][3] = 1 # Black
    
    # Add another white piece to ensure valid move elsewhere if needed
    board[0][0] = 2
    
    return board

def test_agent():
    print("Testing ASPAgent...")
    
    # Ensure dlv.exe exists (mock check)
    if not os.path.exists("dlv.exe"):
        print("WARNING: dlv.exe not found in root. Test might fail if not in PATH.")
    
    agent = ASPAgent()
    board = create_mock_board()
    turn = 2 # White
    
    print("Requesting best move for White (2)...")
    move = agent.get_best_move(board, turn)
    
    if move:
        print(f"SUCCESS: Move returned: {move}")
        # Expect move from (2,2) -> (2,1) or similar
        fx, fy, tx, ty, mtype = move
        if fy == 2 and fx == 2:
            print("Move starts from expected piece.")
        else:
            print("Move starts from unexpected piece (could be 0,0).")
    else:
        print("FAILURE: No move returned.")

if __name__ == "__main__":
    test_agent()
