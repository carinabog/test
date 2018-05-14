import random

body_parts = ["уши", "глаза", "локти", "пятки"]
adjectives = ["унылые", "злые", "противные", "отвисшие"]
animals = ["выдры", "мартышки", "мухи", "капибары", "суслика"]

print(
    "У тебя {adjective} {body_part} как у {animal}!".format(
        adjective=random.choice(adjectives),
        body_part=random.choice(body_parts),
        animal=random.choice(animals),
    )
)

# Написать функцию, которая по переданному списку людей, будет дразнить каждого
def taunt_people(names):
    for name in names:
        print(
            "{name}, у тебя {adjective} {body_part} как у {animal}!".format(
                name=name,
                adjective=random.choice(adjectives),
                body_part=random.choice(body_parts),
                animal=random.choice(animals),
            )
        )

taunt_people(["Вася", "Женя","Дима"])

