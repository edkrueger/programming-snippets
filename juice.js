/**
 * Juices a fruit.
 */
const juice = (pressType, fruit) => {
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

  const compatibleFruitTypes = compatibleFruitTypesLookup[pressType];

  if (!compatibleFruitTypes.has(fruit)) {
    throw Error(
      `fruit must be one of ${Array.from(compatibleFruitTypes).join(", ")}.`
    );
  }

  return `Some fresh ${fruit} juice`;
};

console.log(juice("lemon", "lime"));
console.log(juice("lemon", "lemon"));
console.log(juice("lemon", "orange")); // should throw an error

console.log(juice("pomelo", "pomelo")); // should throw an error
