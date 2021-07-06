def juice(press_type, fruit):
    """Juices a fruit."""
    press_types = {"lime", "lemon", "orange", "grapefruit"}

    if not press_type in press_types:
        raise ValueError(f"press_type must be one of {press_types}")

    compatible_fruit_types_lookup = {
        "lime": {"lime", "lemon"},
        "lemon": {"lime", "lemon"},
        "orange": {"lemon", "orange"},
        "grapefruit": {"grapefruit", "pomelo"},
    }

    compatible_fruit_types = compatible_fruit_types_lookup[press_type]

    if not fruit in compatible_fruit_types:
        raise ValueError(f"fruit must be one of {compatible_fruit_types}")

    return f"Some fresh {fruit} juice."


if __name__ == "__main__":

    print(juice(press_type="lemon", fruit="lime"))
    print(juice(press_type="lemon", fruit="lemon"))
    print(juice(press_type="lemon", fruit="orange"))  # should throw an error

    print(juice(press_type="pomelo", fruit="pomelo"))  # should throw an error
