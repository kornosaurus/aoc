import { promises } from "fs";

const input = (await promises.readFile("./input.txt", { encoding: "utf8" }))
  .split("\n")
  .slice(0, -1)
  .map((v) => v.split(" "));

const mul = (x, y) => x * y;
const add = ([x, y, aim], [x2, y2, aim2]) => [x + x2, y + y2, aim + aim2];

const doCommand = ([command, arg], aim) => {
  const move = parseInt(arg);
  switch (command) {
    case "forward":
      return [move, move * aim, 0];
    case "down":
      return [0, 0, move];
    case "up":
      return [0, 0, -move];
  }
};

const navigate = (commands) =>
  commands.reduce(
    (current, command) => add(current, doCommand(command, current[2])),
    [0, 0, 0]
  );

console.log(`Part 2 answer: ${mul(...navigate(input))}`);
