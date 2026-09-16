#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    for value in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
