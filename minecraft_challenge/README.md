# Minecraft Fence Door Teleporter Minigame

A fun Minecraft minigame that teleports players 300 blocks in the air when they craft a fence door!

## Features

- 🚪 Detects when players craft fence doors
- ⬆️ Teleports players 300 blocks up in the air
- ✨ Particle effects for teleportation
- 💬 Chat notifications
- 🎮 Supports multiple players

## Requirements

- Minecraft (Java Edition)
- Python 3.x
- Minecraft Python API (mcpi)

## Installation

1. Install the Minecraft Python API:
   ```bash
   pip install mcpi
   ```

   Or for Raspberry Pi:
   ```bash
   sudo apt-get install python3-mcpi
   ```

2. Make sure Minecraft is running and the Python API is enabled

## How to Run

1. Start Minecraft
2. Create a world or join a server
3. Run the minigame:
   ```bash
   python MinijuegoPython.py
   ```

## How to Play

1. The game will start automatically when you run the script
2. Craft a fence door using 4 sticks and 2 planks
3. As soon as you craft it, you'll be teleported 300 blocks up in the air!
4. Enjoy the view and try to land safely!

## Controls

- Use normal Minecraft controls to move around
- The teleportation happens automatically when you craft a fence door
- Press Ctrl+C to stop the minigame

## Game Mechanics

- The game continuously monitors all players' inventories
- When a fence door (block ID 96) is detected in a player's inventory
- The player is immediately teleported 300 blocks up
- Particle effects and chat messages provide feedback

## Troubleshooting

- Make sure Minecraft is running before starting the script
- Ensure the Python API is properly connected
- Check that you have the correct permissions in your Minecraft world
- For multiplayer servers, make sure the API is enabled

## Notes

- This minigame works best in creative mode or with flight enabled
- Players will need to be careful not to fall after teleportation
- The game supports multiple players simultaneously
- Each player's inventory is monitored independently

Have fun with your teleportation minigame! 🎮
