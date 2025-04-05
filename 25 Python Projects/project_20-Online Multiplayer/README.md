🎮 Multiplayer Game using Pygame – by Tehmina

📁 Project Files
This project has 4 Python files:

server.py – This file runs the game server. It controls the whole game.

client.py – This file is for players to play the game.

network.py – It handles the connection between client and server.

player.py – It creates the player and handles player movement.

▶️ How to Run the Game
🔧 Step 1: Install Pygame
If you don’t have Pygame, open the terminal and type:

sh
Copy
Edit
pip install pygame
🖥 Step 2: Start the Server
Go to the project folder in your terminal and run:

sh
Copy
Edit
python server.py
You will see:

arduino
Copy
Edit
Server started  
Waiting for connections...
🎮 Step 3: Start the Client (Players)
Now open a new terminal window and run:

sh
Copy
Edit
python client.py
You can run this command in many terminals to play with more players.

⌨️ Step 4: Play the Game
Use arrow keys or W, A, S, D to move your player.

You will see other players moving on the screen.

If the server stops, the game will also close.

🔍 What Each File Does
🧍‍♂️ player.py
Stores the player’s position, size, and color.

Moves the player when keys are pressed.

Keeps the player inside the window.

Draws the player on the screen.

🌐 network.py
Connects the client to the server.

Sends and receives data.

Uses pickle to convert Python data to bytes.

🖧 server.py
Starts the game server.

Waits for players to join.

Gives a unique ID to each player.

Handles data from players.

Sends updates to all players.

Handles player disconnection.

🕹 client.py
Starts the Pygame window.

Connects to the server.

Creates the player.

Handles key presses.

Sends player’s position to the server.

Draws all players on the screen.

⌨️ Game Controls
↑ or W = Move up

↓ or S = Move down

← or A = Move left

→ or D = Move right

Close the window = Quit the game