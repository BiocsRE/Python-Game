
---

# Escape the Abandoned Mansion

## Description
"Escape the Abandoned Mansion" is a simple 2D action-survival game built with Python using the Pygame library. In this game, the player navigates through a dark and eerie mansion filled with zombies. The objective is to survive as long as possible by avoiding or eliminating the zombies while also dealing with random walls that block the path. The player can move, shoot bullets, and try to outsmart the zombies. If the player collides with a zombie, they lose health. The game ends when the player’s health reaches zero.

## Features
- **Player movement**: Use the arrow keys or WASD to move around the screen.
- **Shooting**: Press the spacebar to shoot bullets in the direction you're facing.
- **Zombies**: Zombies move toward the player and appear randomly around the map.
- **Walls**: Randomly placed walls block the player’s movement and add challenge.
- **Health & Score**: The player has a health bar and the score increases as they eliminate zombies.
- **Game Over & Restart**: The game ends when the player’s health reaches zero, and you can press 'R' to restart.

## Requirements

To run this game, you’ll need Python 3 and the Pygame library installed.

1. Install Python: [Python Downloads](https://www.python.org/downloads/)
2. Install Pygame: Run the following command in your terminal or command prompt:
   ```bash
   pip install pygame
   ```

## How to Play

1. **Move the Player**: Use the **arrow keys** or **WASD** to move the player.
2. **Shoot Bullets**: Press **spacebar** to shoot bullets in the direction you're facing.
3. **Avoid Zombies**: Zombies move toward the player and deal damage when they collide with you. Try to avoid them!
4. **Walls**: Random walls are placed throughout the level. Use them for cover, but also be careful not to get trapped.
5. **Health**: Your health is displayed at the top left corner of the screen. If your health drops to zero, it’s game over.
6. **Score**: Your score increases each time you eliminate a zombie. Try to survive as long as possible!

### Game Controls:
- **W/A/S/D** or **Arrow Keys**: Move the player
- **Spacebar**: Shoot bullets
- **R**: Restart the game after game over
- **Q**: Quit the game

## How to Run

1. Clone this repository to your local machine:
   ```bash
   https://github.com/BiocsRE/escape-the-abandoned-mansion.git
   ```
2. Navigate to the project directory:
   ```bash
   cd escape-the-abandoned-mansion
   ```
3. Run the game script:
   ```bash
   python game.py
   ```

## Game Loop

The game consists of the following main components:
1. **Player Class**: Handles player movement, shooting, health, and rendering.
2. **Zombie Class**: Zombies spawn randomly, move toward the player, and deal damage on collision.
3. **Bullet Class**: Bullets move in the direction the player is facing and destroy zombies upon collision.
4. **Wall Class**: Randomly generated walls that add obstacles to the gameplay.
5. **Game Over & Restart**: When health reaches zero, the game is over, and you can press 'R' to restart.

## Contributions

Feel free to fork and modify the game! Contributions are welcome.

To contribute, please fork the repository, create a new branch, and submit a pull request with your changes.

### Notes:
- The file is structured to provide a clear explanation of the game, installation steps, and controls.
- Make sure to replace the GitHub link (`https://github.com/BiocsRE/escape-the-abandoned-mansion.git`) with the actual link to your repository.

This `README.md` should provide users with all the information they need to run and enjoy the game.

![image](https://github.com/user-attachments/assets/236a57f3-1d94-464a-a2b2-fcfdda799207)
![image](https://github.com/user-attachments/assets/702f93a7-3cdf-42ee-a569-f4215033afe7)
