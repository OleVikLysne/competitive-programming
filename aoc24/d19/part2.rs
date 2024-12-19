use std::collections::HashMap;

fn solve(pattern: &[char], towels: &[Vec<char>], i: usize, mem: &mut HashMap<usize, u64>) -> u64 {
    if i == pattern.len() {
        return 1
    }
    if let Some(res) = mem.get(&i) {
        return *res
    }
    let mut res = 0;
    for towel in towels {
        if pattern.len() - i < towel.len() {
            continue
        }
        if towel == &pattern[i..i+towel.len()] {
            res += solve(pattern, towels, i+towel.len(), mem);
        }
    }
    mem.insert(i, res);
    return res
}

fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let towels: Vec<Vec<char>> = buf.split_ascii_whitespace().map(|x| x.trim_end_matches(",").chars().collect()).collect();
    let _ = stdin.read_line(&mut buf);
    let mut total = 0;
    for pattern in stdin.lines().map(|x| x.unwrap().chars().collect::<Vec<char>>()) {
        total += solve(&pattern, &towels, 0, &mut HashMap::new())
    }
    println!("{}", total);
}