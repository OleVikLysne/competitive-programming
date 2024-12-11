use std::collections::HashMap;

fn check(x: u64) -> Option<(u64, u64)> {
    for i in 1.. {
        if 10_u64.pow(i) > x {
            if i % 2 == 0 {
                let base = 10_u64.pow(i / 2);
                return Some((x / base, x % base));
            }
            break;
        }
    }
    return None;
}

fn dp(i: i32, x: u64, mem: &mut HashMap<(u64, i32), u64>, t: i32) -> u64 {
    if i == t {
        return 1;
    }
    if let Some(val) = mem.get(&(x, i)) {
        return *val;
    }
    let res = {
        if x == 0 {
            dp(i + 1, 1, mem, t)
        } else if let Some((l, r)) = check(x) {
            dp(i + 1, l, mem, t) + dp(i + 1, r, mem, t)
        } else {
            dp(i + 1, x * 2024, mem, t)
        }
    };
    mem.insert((x, i), res);
    return res;
}

fn main() {
    let mut buf = String::new();
    let _ = std::io::stdin().read_line(&mut buf);
    let seq: Vec<u64> = buf
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let mut mem = HashMap::new();
    let mut total = 0;
    for x in seq {
        total += dp(0, x, &mut mem, 75)
    }
    println!("{}", total)
}
