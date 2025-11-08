from .enemy import Enemy

class Boss(Enemy):
    def __init__(self):
        super().__init__(
            name="Boss",
            img_path="images/boss.png",
            width=100,
            height=100,
            x= 600 - 100 // 2,
            y=50,
            health=30,
            fires_projectiles=True
        )
