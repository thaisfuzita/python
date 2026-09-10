import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb']
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    gen1 = gen_event()
    for i in range(1, 1000):
        (player, action) = next(gen1)
        print(f"Event {i}: Player {player} did action {action}")

    events = []
    gen2 = gen_event()
    for j in range(1, 10):
        events.append(next(gen2))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains from list: {events}")


if __name__ == "__main__":
    ft_data_stream()
