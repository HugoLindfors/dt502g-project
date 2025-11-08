from .enemy import Enemy

class Slime(Enemy):
    slime_counter = 0

    def __init__(self, x=50, y=50):
        Slime.slime_counter += 1
        super().__init__(
            name=f"Slime{Slime.slime_counter}",
            img_path="images/slime.png",
            width=50,  # Smaller size
            height=50,
            x=x,
            y=y,
            health=1,
            fires_projectiles=False
        )
