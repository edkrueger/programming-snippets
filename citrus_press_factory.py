def citrus_press_factory(press_type):
    """Creates a citrus press."""
    press_types = {"lime", "lemon", "orange", "grapefruit"}

    if not press_type in press_types:
        raise ValueError(f"press_type must be one of {press_type}")

    compatible_fruit_types_lookup = {
        "lime": {"lime", "lemon"},
        "lemon": {"lime", "lemon"},
        "orange": {"lemon", "orange"},
        "grapefruit": {"grapefruit", "pomelo"},
    }

    def citrus_press(fruit):
        """Makes fresh juice from a fruit."""
        compatible_fruit_types = compatible_fruit_types_lookup[press_type]

        print(compatible_fruit_types)

        if not fruit in compatible_fruit_types:
            raise ValueError(f"fruit must be one of {compatible_fruit_types}")

        return f"Some fresh {fruit} juice."

    return citrus_press


if __name__ == "__main__":

    lemon_press = citrus_press_factory("lemon")
    print(lemon_press("lime"))
    print(lemon_press("lemon"))
    print(lemon_press("orange"))  # should throw an error

    pomelo_press = citrus_press_factory("pomelo")  # should throw an error
