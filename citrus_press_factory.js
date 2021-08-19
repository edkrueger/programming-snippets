/**
 * Creates a citrus press.
 */
const citrusPressFactory = (pressType) => {
  const pressTypes = new Set(["lime", "lemon", "orange", "grapefruit"]);

  if (!pressTypes.has(pressType)) {
    throw Error(
      `pressType must be one of ${Array.from(pressTypes).join(", ")}).`
    );
  }

  compatibleFruitTypesLookup = {
    lime: new Set(["lime", "lemon"]),
    lemon: new Set(["lime", "lemon"]),
    orange: new Set(["lemon", "orange"]),
    grapefruit: new Set(["grapefruit", "pomelo"]),
  };

  /**
   * Makes fresh juice from a fruit.
   */
  const citrusPress = (fruit) => {
    const compatibleFruitTypes = compatibleFruitTypesLookup[pressType];

    if (!compatibleFruitTypes.has(fruit)) {
      throw Error(
        `fruit must be one of ${Array.from(compatibleFruitTypes).join(", ")}.`
      );
    }

    return `Some fresh ${fruit} juice`;
  };

  return citrusPress;
};

const lemonPress = citrusPressFactory("lemon");
console.log(lemonPress("lime"));
console.log(lemonPress("lemon"));
console.log(lemonPress("orange")); // should throw an error

const pomeloPress = citrusPressFactory("pomelo"); // should throw an error
