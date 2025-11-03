from entities import Entity
import threading
import time

class Enemy(Entity):
    fire_delay = 3  # seconds between firing projectiles
    max_x_leftright_move = 10  # max horizontal move distance

    def __init__(self, health: int, x: int, y: int):
        super().__init__()

        # Basic attributes
        self.health = health
        self.spawn_x = x
        self.spawn_y = y
        self.maximum_allowed_right_x = x + self.max_x_leftright_move
        self.minimum_allowed_left_x = x - self.max_x_leftright_move

        # Movement and control
        self.x_moving_direction = -1
        self.y_moving_direction = 0
        self.alive_event = threading.Event()  # controls lifetime
        self.health_lock = threading.Lock()

        self.setPosition(x, y)

        # Start behavior threads
        self.move_thread = threading.Thread(target=self.move, daemon=True)
        self.fire_thread = threading.Thread(target=self.fire, daemon=True)
        self.alive_thread = threading.Thread(target=self.alive, daemon=True)

        self.move_thread.start()
        self.fire_thread.start()
        self.alive_thread.start()

    def move(self):
        while not self.alive_event.is_set():
            if self.x <= self.minimum_allowed_left_x:
                self.x_moving_direction = 1
            elif self.x >= self.maximum_allowed_right_x:
                self.x_moving_direction = -1

            self.x += self.x_moving_direction
            self.y += self.y_moving_direction
            time.sleep(1 / 60)  # simulate frame rate

    def alive(self):
        while not self.alive_event.is_set():
            with self.health_lock:
                if self.health <= 0:
                    # Stop all activity
                    self.alive_event.set()
                    # TODO: turn the entity into a scrap
                    break
            time.sleep(1 / 60)

    def fire(self):
        while not self.alive_event.is_set():
            # TODO: Implement projectile firing
            time.sleep(self.fire_delay)

    def hit(self):
        """Called when the enemy is hit by a projectile."""
        with self.health_lock:
            self.health -= 1

    def getHealth(self):
        with self.health_lock:
            return self.health

    def setHealth(self, health: int):
        with self.health_lock:
            self.health = health
