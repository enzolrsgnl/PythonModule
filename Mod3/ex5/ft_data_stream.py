import typing
import random

players = ["Charlie", "Dylan", "Paul", "Alice", "John"]
actions = ["attacks", "jump", "grab", "eat", "run", "sleep", "swim", "climb", "release"]

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:    # creation d une boucle infinie 
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)

def consume_event(list_event: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(list_event) > 0:
        index = random.randrange(0, len(list_event))
        poped = list_event.pop(index)
        yield poped
       


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()   # creation du generator 
    
    for _ in range(1000):   # _ car pas besoin de vakleur pour boucler grace au generateur 
        event = next(generator)    #utilisation du generator
        print(event)
    
    list_event = []
    for _ in range(10):
        new_event = next(generator)    #utilisation du generator
        list_event.append(new_event)
    print("Built list of 10 events: " + str(list_event))

    for event in consume_event(list_event):  #pour chaque element contenu dans consume event a qui on a donné la liste, on supprime un element 
        print("Got event from list: " + str(event))
        print("Remains in list: " + str(list_event))
