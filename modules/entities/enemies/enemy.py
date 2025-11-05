from entities import Entity
from entities.items import Item
from entities.items import Scrap
import threading
import time

"""enemy.py: A template for creating enemy entities."""

__author__ = "Gustav Vising"


class Enemy(Entity):

    tick = 1 / 60  # Sleep delay for updating the enemy

    # Variables that will be initialized
    enemy_health = -1
    enemy_spawn_position_x = -1
    enemy_spawn_position_y = -1
    enemy_maximum_allowed_right = -1
    enemy_maximum_allowed_left = -1

    # Constants
    enemy_delay_between_fire = 3  # Seconds between firing projectiles
    enemy_maximum_horizontal_movement = (
        10  # Both left and right from the spawn position
    )
    enemy_y_moving_direction = -1  # The enemy moves downwards

    # Changing variables
    enemy_x_moving_direction = -1

    def __init__(
        self,
        name: str,
        img_path: str,
        width: int,
        height: int,
        x: int,
        y: int,
        health: int,
    ):
        super().__init__()

        # Entity class variables
        self.name = name
        self.img_path = img_path
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Enemy class variables
        self.enemy_health = health
        self.enemy_spawn_position_x = x
        self.enemy_spawn_position_y = y

        # Calculate values
        self.enemy_maximum_allowed_right = x + self.enemy_maximum_allowed_right
        self.enemy_maximum_allowed_left = x - self.enemy_maximum_allowed_left

        # Spawn position
        self.setPosition(x, y)

        # Events
        self.alive_event = threading.Event()
        self.health_lock = threading.Lock()

        self.move_thread = threading.Thread(target=self.move, daemon=True)
        self.fire_thread = threading.Thread(target=self.fire, daemon=True)
        self.alive_thread = threading.Thread(target=self.alive, daemon=True)

        self.move_thread.start()
        self.fire_thread.start()
        self.alive_thread.start()

    """ Update the enemy location """

    def move(self):
        while not self.alive_event.is_set():
            if self.x <= self.enemy_maximum_allowed_left:
                self.enemy_x_moving_direction = 1
            elif self.x >= self.enemy_maximum_allowed_right:
                self.enemy_x_moving_direction = -1

            self.x += self.enemy_x_moving_direction
            self.y += self.enemy_y_moving_direction
            time.sleep(self.tick)

    """ Lifetime of the enemy """

    def alive(self):
        while not self.alive_event.is_set():
            with self.health_lock:
                if self.enemy_health <= 0:
                    # Stop all activity for the enemy
                    self.alive_event.set()
                    # Turn the enemy into a scrap
                    scrap = Scrap(Item())
                    scrap.x = self.x
                    scrap.y = self.y
                    # Remove the enemy
                    # Code to access the entity list and remove the enemy goes here
                    break
            time.sleep(self.tick)

    """ The enemy fires projectiles to attack the player """

    def fire(self):
        while not self.alive_event.is_set():
            # TODO: Implement projectile firing
            time.sleep(self.enemy_delay_between_fire)

    """Called when the enemy is hit by a projectile."""

    def hit(self):
        with self.health_lock:
            self.enemy_health -= 1

    def getHealth(self):
        with self.health_lock:
            return self.enemy_health

    def setHealth(self, health: int):
        with self.health_lock:
            self.enemy_health = health
