# Chess
A simple desktop chess application that supports chess engine import and local multiplayer.

![](https://raw.githubusercontent.com/mandrews6975/Chess/master/readme_img/04.PNG)

# Guide
Chess is not currently available in a single executable file; however, running Chess is quite simple. Requirements for running Chess are described in the `requirements.txt` file, which is quite short. Once all dependencies are installed on your machine, simply run `python main.py` to open Chess. 
You will be greeted with this window upon opening Chess.

![](https://raw.githubusercontent.com/mandrews6975/Chess/master/readme_img/01.PNG)

This application supports human vs. human, human vs. engine and engine vs. engine gameplay. **Note: This application only supports UCI chess engines such as [Stockfish](https://stockfishchess.org/).** The controls toward the top of the window are used to configure a new game. Clicking the menu button in the top left corner of the screen will open the options menu, allowing you to adjust engine processing time limits as seen below.

![](https://raw.githubusercontent.com/mandrews6975/Chess/master/readme_img/02.PNG)

After configuring your game, clicking the "New Game" button will launch a new game with your configurations. If two engines are playing, the game will begin immediately and continue until either a new game is launched or the engine vs. engine game finishes. If at least one human is playing, the window will appear similar to the window below.

![](https://raw.githubusercontent.com/mandrews6975/Chess/master/readme_img/03.PNG)

Humans make moves by typing their moves into the text input below the board. The move format must be: "start_square""end_square" (no space in between squares; ex: e2e4, g1f3, etc.). If a hint is desired, one can press the "Hint" button to have the built-in Stockfish engine find its best move for the current player's turn and automatically enter it in the move input text box as seen below.

![](https://raw.githubusercontent.com/mandrews6975/Chess/master/readme_img/04.PNG)

As the game continues, the game's PGN will be generated on the right side of the window. If one desires to export the PGN, simply click the "Export" button to save the PGN to a directory on your machine.
