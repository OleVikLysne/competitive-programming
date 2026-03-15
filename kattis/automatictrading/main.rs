fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let sequence: Vec<u8> = buf.trim().chars().map(|x| x as u8).collect();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let q: u32 = buf.trim().parse().unwrap();
    for _ in 0..q {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut coord_iter = buf.split_ascii_whitespace();
        let i: u32 = coord_iter.next().unwrap().parse().unwrap();
        let j: u32 = coord_iter.next().unwrap().parse().unwrap();
        let mut x = i as usize;
        let mut y = j as usize;
        while y < sequence.len() && sequence[x] == sequence[y] {
            x += 1;
            y += 1;
        }
        let count = x as u32 - i;
        println!("{}", count);
    }
}