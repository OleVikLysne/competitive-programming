use std::collections::HashMap;
fn foo(mut mem: &mut HashMap<(u16,u16), bool>, b: u16, d: u16) -> bool {
    if mem.contains_key(&(b, d)) {
        return mem[&(b, d)];
    }
    if b*2 < d {
        mem.insert((b, d), true);
        return true;
    }
    if d*2 < b {
        mem.insert((b, d), false);
        return false;
    }
    if mem.contains_key(&(b/2, d/2)) {
        mem.insert((b, d), mem[&(b/2,d/2)]);
        return mem[&(b,d)];
    }

    for i in 1..(d/2)+1 {
        if !foo(&mut mem, i, b) && !foo(&mut mem, d-i, b) {
            mem.insert((b, d), true);
            return true;
        }
    }
    mem.insert((b, d), false);
    return false
}

fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let n = buf.trim().parse::<u8>().unwrap();
    let mut mem: HashMap<(u16, u16), bool> = HashMap::new(); 
    mem.insert((1,1), false);
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut line = buf.split_whitespace();
        let b: u16 = line.next().unwrap().parse().unwrap();
        let d: u16 = line.next().unwrap().parse().unwrap();
        let person: String = line.next().unwrap().parse().unwrap();
        let res: bool;
        if person == "Harry" {
            res = foo(&mut mem, b, d);
        }
        else {
            res = foo(&mut mem, d, b);
        }
        if res {
            println!("{} can win", person);
        }
        else {
            println!("{} cannot win", person);
        }
    }

}
