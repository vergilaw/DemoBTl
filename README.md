# Go Game 2D  

## Introduction  
This is a 2D Go game with a top-down view, developed in Python. The game supports:  
- Playing against a bot using the Monte Carlo Tree Search (MCTS) algorithm (to be implemented).  
- 1v1 mode for two human players.  

## Key Features  
- **Intuitive 2D Interface**: Clearly displays the board and stones.  
- **Game Modes**:  
  - Play against another human on the same device.  
- **Rule Enforcement**: Automatically checks valid moves, captures stones, and calculates scores.  

## Installation  
### System Requirements  
- Python 3.8 or later  
- Required libraries:  
  ```sh
  pip install pygame numpy
  ```  

## Usage Guide  
### Running the Game  
Open a terminal or command prompt and run:  
```sh
python main.py
```  

### How to Play  
- **1v1 Mode**: Two players take turns placing black and white stones.  
- **1vAI Mode**: Choose difficulty level (Easy/Medium/Hard).  
- **AIvAI Mode**: AI vs AI (MCTS vs Alpha-Beta Pruning).  
- Click on an empty spot to place a stone.  
- The game ends when no more moves are possible or when both players pass consecutively.  
