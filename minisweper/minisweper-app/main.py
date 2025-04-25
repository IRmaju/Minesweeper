import streamlit as st
import random

def generate_board(size, bombs):
    # Initialize an empty board
    board = [[' ' for _ in range(size)] for _ in range(size)]
    bomb_positions = set()

    # Randomly place bombs on the board
    while len(bomb_positions) < bombs:
        r, c = random.randint(0, size-1), random.randint(0, size-1)
        bomb_positions.add((r, c))

    # Set numbers around bombs
    for r in range(size):
        for c in range(size):
            if (r, c) not in bomb_positions:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < size and 0 <= nc < size and (nr, nc) in bomb_positions:
                            count += 1
                board[r][c] = str(count) if count > 0 else ' '

    return board, bomb_positions

def display_board(board):
    for row in board:
        st.write(" | ".join(row))

def main():
    size = st.number_input("Enter board size:", min_value=5, max_value=10, value=5)
    bombs = st.number_input("Enter number of bombs:", min_value=1, max_value=size*size//2, value=3)
    
    board, bomb_positions = generate_board(size, bombs)
    
    st.title("Minesweeper Game")
    st.write("Board Size:", size, "x", size)
    
    # Display the board
    display_board(board)

    # Add interactive gameplay (simple version)
    clicked_position = st.text_input("Enter position to reveal (row,col):", "")
    
    if clicked_position:
        try:
            r, c = map(int, clicked_position.split(','))
            if (r, c) in bomb_positions:
                st.error("💣 You hit a bomb! Game Over!")
            else:
                st.success(f"Safe! Value at ({r},{c}): {board[r][c]}")
        except:
            st.error("Invalid input. Please enter row,col in format 'row,col'.")

if __name__ == "__main__":
    main()
