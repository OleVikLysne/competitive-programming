fn main() {
    let mut v1 = Vec::new();
    let mut v2 = Vec::new();
    let stdin = std::io::stdin();
    for line in stdin.lines().map(|x| x.unwrap()) {
        let mut foo = line.split_ascii_whitespace();
        let a: i32 = foo.next().unwrap().parse().unwrap();
        let b: i32 = foo.next().unwrap().parse().unwrap();
        v1.push(a);
        v2.push(b);
    }
    v1.sort();
    v2.sort();
    let s = std::iter::zip(v1.iter(), v2.iter()).fold(0, |acc, (a, b)| acc + (*a-*b).abs());
    println!("{}", s);
}
