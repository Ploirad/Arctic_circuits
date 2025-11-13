#!/usr/bin/env python3
"""
Minecraft Minigame: Fence Door Teleporter
When a player crafts a fence door, they get teleported 300 blocks in the air!
"""

import time
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

class EscapeRoom:
    def __init__(self):
        """Initialize the minigame"""
        self.mc = minecraft.Minecraft.create()
        self.mc.postToChat("Escape Room Minigame Started!")
        self.mc.postToChat("Craft the correct block and use it properly to exit the room and win the game!")
        
        # Small delay to ensure connection is ready
        time.sleep(0.5)
        
        # Track player positions to detect crafting
        self.player_positions = {}
        # Track discovered fence gates to detect newly placed ones
        self.known_gate_positions = set()
        # Track if initial teleport has been done
        self.initial_teleport_done = False
    
    def teleport_to_start(self):
        """Teleport player to starting location at x=1179, y=5, z=125"""
        try:
            # Use ints for broader compatibility across mcpi variants (same as teleport_player_up)
            start_x, start_y, start_z = int(1179), int(1), int(125)
            
            # Get all player positions (same approach as get_player_positions)
            try:
                player_ids = self.mc.getPlayerEntityIds()
                for player_id in player_ids:
                    try:
                        # Use the same teleport method as teleport_player_up
                        if player_id == 0:
                            # Single-player API path
                            self.mc.player.setPos(start_x, start_y, start_z)
                        else:
                            # Multi-player entity path
                            self.mc.entity.setPos(player_id, start_x, start_y, start_z)
                    except Exception:
                        # Last-resort fallback (same as teleport_player_up)
                        self.mc.player.setPos(start_x, start_y, start_z)
            except:
                # Fallback to single player (same as get_player_positions)
                try:
                    self.mc.player.setPos(start_x, start_y, start_z)
                except Exception as e:
                    print(f"Error teleporting player to start: {e}")
            
            self.mc.postToChat("Teleported to starting location!")
                    
        except Exception as e:
            print(f"Error in teleport_to_start: {e}")
        
    def get_player_positions(self):
        """Get all player positions"""
        try:
            # Get all players (this might need adjustment based on your server setup)
            player_ids = self.mc.getPlayerEntityIds()
            positions = {}
            
            for player_id in player_ids:
                try:
                    pos = self.mc.entity.getPos(player_id)
                    positions[player_id] = pos
                except:
                    continue
                    
            return positions
        except:
            # Fallback to single player
            try:
                pos = self.mc.player.getPos()
                return {0: pos}
            except:
                return {}
    
    def placed_fence_gate_near(self, pos):
        """Detect if a new fence gate has been placed near a position.

        mcpi/RaspberryJuice does not expose inventory/crafting APIs, so we
        simulate the minigame by detecting newly placed fence gates near
        the player. If a new fence gate block appears that we have not
        seen before, treat that as the trigger.
        """
        try:
            # Numeric ID for oak fence gate in classic IDs
            FENCE_GATE_ID = 107
            radius_xz = 4
            radius_y = 3
            base_x, base_y, base_z = int(pos.x), int(pos.y), int(pos.z)
            found_new_gate = False

            for dx in range(-radius_xz, radius_xz + 1):
                for dy in range(-radius_y, radius_y + 1):
                    for dz in range(-radius_xz, radius_xz + 1):
                        x = base_x + dx
                        y = base_y + dy
                        z = base_z + dz
                        block_id = self.mc.getBlock(x, y, z)
                        if block_id == FENCE_GATE_ID:
                            key = (x, y, z)
                            if key not in self.known_gate_positions:
                                # New fence gate detected
                                self.known_gate_positions.add(key)
                                found_new_gate = True
            return found_new_gate
        except Exception as e:
            print(f"Error detecting fence gate placement: {e}")
            return False
    
    def teleport_player_up(self, player_id, pos):
        """Teleport player 300 blocks up"""
        try:
            # Calculate new position (300 blocks up)
            # Use ints for broader compatibility across mcpi variants
            new_x, new_y, new_z = int(pos.x), int(pos.y + 300), int(pos.z)
            
            # Teleport the player
            try:
                if player_id == 0:
                    # Single-player API path
                    self.mc.player.setPos(new_x, new_y, new_z)
                else:
                    # Multi-player entity path
                    self.mc.entity.setPos(player_id, new_x, new_y, new_z)
            except Exception:
                # Last-resort fallback
                self.mc.player.setPos(new_x, new_y, new_z)
            
            # Send messages without relying on entity IDs/names (varies by API)
            who = "You" if player_id == 0 else "A player"
            self.mc.postToChat(f"{who} placed a fence gate!")
            self.mc.postToChat("Teleporting 300 blocks up!")
            self.mc.postToChat("Enjoy the view!")
            
            # Add some particles for effect
            self.create_teleport_effect(Vec3(new_x, new_y, new_z))
            
        except Exception as e:
            print(f"Error teleporting player: {e}")
    
    def create_teleport_effect(self, pos):
        """Create particle effects at teleport location"""
        try:
            # Create some particles around the player
            for i in range(10):
                offset_x = (i - 5) * 2
                offset_z = (i - 5) * 2
                effect_pos = Vec3(pos.x + offset_x, pos.y, pos.z + offset_z)
                self.mc.spawnParticle(effect_pos, "explode")
        except:
            pass  # Particle effects are optional
    
    def run_game(self):
        """Main game loop"""
        print("Escape Room Minigame is running!")
        print("Press Ctrl+C to stop the game")
        
        try:
            while True:
                # Get all player positions
                current_positions = self.get_player_positions()
                
                # Do initial teleport if not done yet and player is detected
                if not self.initial_teleport_done and current_positions:
                    self.teleport_to_start()
                    self.initial_teleport_done = True
                    time.sleep(1.0)  # Give time for teleport to complete
                
                # Check each player for newly placed fence gates nearby
                for player_id, pos in current_positions.items():
                    if self.placed_fence_gate_near(pos):
                        self.teleport_player_up(player_id, pos)
                
                # Update player positions
                self.player_positions = current_positions
                
                # Wait a bit before checking again
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\nGame stopped by user")
            self.mc.postToChat("Escape Room Minigame stopped!")
        except Exception as e:
            print(f"Game error: {e}")
            self.mc.postToChat("Game encountered an error!")

def main():
    """Main function to start the minigame"""
    try:
        # Create and run the minigame
        game = EscapeRoom()
        game.run_game()
    except Exception as e:
        print(f"Failed to start game: {e}")
        print("Make sure Minecraft is running and the Python API is connected!")

if __name__ == "__main__":
    main()
