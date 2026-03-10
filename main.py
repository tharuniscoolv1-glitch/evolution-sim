
from world import World


def main():
    
    world = World(width=100, height=100, population=150)
    world.run(days=50, sleep_time=0.1)


if __name__ == "__main__":
    main()
