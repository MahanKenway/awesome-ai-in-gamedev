class EnemyAI:
    def __init__(self):
        self.state = "IDLE"
        self.player_distance = 100

    def update(self, player_dist):
        self.player_distance = player_dist
        
        if self.state == "IDLE":
            print("Enemy is resting...")
            if self.player_distance < 50:
                self.state = "CHASE"
                print("!!! Player spotted! Switching to CHASE mode.")
                
        elif self.state == "CHASE":
            print("Enemy is chasing the player!")
            if self.player_distance < 5:
                self.state = "ATTACK"
                print(">>> Within range! Switching to ATTACK mode.")
            elif self.player_distance > 60:
                self.state = "IDLE"
                print("... Player lost. Going back to IDLE.")
                
        elif self.state == "ATTACK":
            print("Enemy is attacking!")
            if self.player_distance > 10:
                self.state = "CHASE"
                print("Player is moving away. Back to CHASE.")

# Simulation
if __name__ == "__main__":
    ai = EnemyAI()
    distances = [100, 40, 30, 4, 15, 70]
    for d in distances:
        print(f"\nDistance to player: {d}")
        ai.update(d)
