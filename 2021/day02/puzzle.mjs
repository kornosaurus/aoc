import { promises } from "fs";

const input = (await promises.readFile("./input.txt", { encoding: "utf8" }))
  .split("\n")
  .slice(0, -1)
  .map((v) => v.split(" "));

const mul = (x, y) => x * y
const add = ([x, y], [x2, y2]) => [x + x2, y + y2]

const doCommand = ([direction, length]) => {
  switch (direction) {
    case "forward":
      return [parseInt(length), 0]
    case "down":
      return [0, parseInt(length)]
    case "up":
      return [0, -parseInt(length)]
  }
}

const navigate = (commands) => commands.reduce((position, command) => add(position, doCommand(command)), [0, 0])

console.log(`Part 1 answer: ${mul(...navigate(input))}`)
