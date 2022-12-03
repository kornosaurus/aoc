import { promises } from "fs";

const win = {
    X: "C",
    Y: "A",
    Z: "B",
    A: "Z",
    B: "X",
    C: "Y"
}

const input = await promises.readFile("./input.txt", { encoding: "utf8" });
const rounds = input.trim().split("\n").map((r) => r.split(" "))

function calcScore(opponent, me) {
    const shapeScore = Object.keys(win).indexOf(me) + 1
    if (win[opponent] === me) {
        return 0 + shapeScore
    } else if (win[me] === opponent) {
        return 6 + shapeScore
    }
    return 3 + shapeScore
}

const score1 = rounds.reduce((acc, round) => acc + calcScore(...round), 0)

console.log(`Part 1: ${score1}`)

function selectShape(opponent, outcome) {
    switch(outcome) {
        case "X":
            return win[opponent]
        case "Y":
            return opponent
    }
    return Object.entries(win).find(([, loss]) => loss === opponent)[0]
}

const score2 = rounds.reduce((acc, [opponent, outcome]) => acc + calcScore(opponent, selectShape(opponent, outcome)), 0)

console.log(`Part 2: ${score2}`)
