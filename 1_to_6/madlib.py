
import random

adjectives = ['thrilling', 'bizarre', 'peaceful', 'stormy', 'glowing']
places = ['ancient castle', 'space station', 'enchanted forest', 'underwater city', 'volcano island']
activities = ['searching for treasure', 'talking to aliens', 'riding dragons', 'building robots', 'escaping lava']

def main():
    friend = input("Enter your friend's name: ")

    place = random.choice(places)
    adjective = random.choice(adjectives)
    activity = random.choice(activities)

    story = f"""
    Last summer, I went on a trip with my best friend {friend}.
    We ended up in a {adjective} place called the {place}.
    While we were there, we spent our days {activity}.
    It was an experience we'll never forget!
    """

    print("\n--- My Crazy Adventure Mad Libs ---")
    print(story)

if __name__ == "__main__":
    main()
