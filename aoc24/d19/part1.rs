fn solve(pattern: &[char], towels: &[Vec<char>], i: usize) -> bool {
    if i == pattern.len() {
        return true
    }
    for towel in towels {
        if pattern.len() - i < towel.len() {
            continue
        }
        if towel == &pattern[i..i+towel.len()] {
            if solve(pattern, towels, i+towel.len()) {
                return true
            }
        }
    }
    return false
}

fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let towels: Vec<Vec<char>> = buf.split_ascii_whitespace().map(|x| x.trim_end_matches(",").chars().collect()).collect();
    let _ = stdin.read_line(&mut buf);
    let mut total = 0;
    for pattern in stdin.lines().map(|x| x.unwrap().chars().collect::<Vec<char>>()) {
        if solve(&pattern, &towels, 0) {
            total += 1;
        }
    }
    println!("{}", total);
}