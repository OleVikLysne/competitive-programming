use std::collections::HashMap;

fn main() {
    let mut v1 = Vec::new();
    let mut counter = HashMap::new();
    let stdin = std::io::stdin();
    for line in stdin.lines().map(|x| x.unwrap()) {
        let mut foo = line.split_ascii_whitespace();
        let a: i32 = foo.next().unwrap().parse().unwrap();
        let b: i32 = foo.next().unwrap().parse().unwrap();
        v1.push(a);
        *counter.entry(b).or_insert(0) += 1;
    }
    let s: i32 = v1.iter().map(|x| *x * *counter.entry(*x).or_default()).sum();
    println!("{}", s)
}
