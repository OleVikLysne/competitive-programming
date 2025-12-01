fn main() {
    let mut buf = String::new();
    let _ = std::io::stdin().read_line(&mut buf);
    let mut seq: Vec<String> = buf.split_ascii_whitespace().map(|x| x.to_string()).collect();

    for _ in 0..25 {
        let mut new = Vec::new();
        for x in seq {
            if x == "0" {
                new.push("1".to_string());
            } else if x.len() % 2 == 0 {
                let (l, mut r) = x.split_at(x.len()/2);
                new.push(l.to_string());
                while r.len() > 1 {
                    if let Some(x) = r.strip_prefix("0") {
                        r = x;
                    } else {break}
                }
                if r.len() > 0 {
                    new.push(r.to_string());
                }
            } else {
                let y: u64 = (x.parse::<u64>().unwrap()) * 2024;
                new.push(y.to_string());
            }
        }
        seq = new;
    }
    println!("{}", seq.len());
}
