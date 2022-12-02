import { promises } from "fs";

const input = (await promises.readFile("./day01.input.txt", { encoding: "utf8" }))
  .split("\n")
  .map((measurment) => parseInt(measurment))
  .slice(0, -1)

const increases = (nums) =>
  nums
    .slice(1)
    .map((curr, i) => (curr > nums[i] ? 1 : 0))
    .reduce((x, y) => x + y, 0);

const sum3 = (nums) =>
  nums
    .slice(2)
    .reduce((acc, _, i) => [...acc, nums.slice(i, i + 3)], [])
    .map((chunk) => chunk.reduce((acc, num) => acc + num, 0))

console.log(`Part 1 answer is: ${increases(input)}`);
console.log(`Part 2 answer is: ${increases(sum3(input))}`);




