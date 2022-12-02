fn part_one() {
    let input = include_str!("../input.txt");

    let solution = input
        .split("\n\n")
        .map(|c| c.lines().map(|cal| cal.parse::<i32>().unwrap()).sum::<i32>())
        .max()
        .unwrap();

    println!("Part one: {}", solution);
}

fn part_two() {
    let input = include_str!("../input.txt");

    let mut calories = input
        .split("\n\n")
        .map(|c| c.lines().map(|cal| cal.parse::<u32>().unwrap()).sum::<u32>())
        .collect::<Vec<u32>>();

    calories.sort();
    let solution = calories.iter().rev().take(3).sum::<u32>();

    println!("Part two: {}", solution);
}

fn main() {
    part_one();
    part_two();
}
