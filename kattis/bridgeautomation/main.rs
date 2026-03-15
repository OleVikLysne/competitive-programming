use std::collections::HashMap;

fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: i32 = buf.trim().parse().unwrap();
    if n == 1 {
        println!("140");
        return;
    }
    let mut boats: Vec<i32> = Vec::with_capacity(n as usize);
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        boats.push(buf.trim().parse().unwrap());
    }
    let mut mem: HashMap<(usize, i32), i32> = HashMap::new();
    println!("{}", 120+20*n+foo(&boats, &mut mem, 1, boats[0]+1820));
}

fn foo(boats: &Vec<i32>, mem: &mut HashMap<(usize, i32), i32>, i: usize, deadline: i32) -> i32 {
    if let Some(cached) = mem.get(&(i, deadline)) {
        return *cached;
    };

    let option1: i32 = std::cmp::max(0, boats[i]-deadline);
    let option2: i32 = 120;
    let ret: i32 = 
        if i == boats.len()-1 {
            std::cmp::min(option1, option2)
        } else {
        std::cmp::min(
            option1 + foo(boats, mem, i+1, deadline+option1+20),
            option2 + foo(boats, mem, i+1, boats[i]+1820)
        )
    };
    mem.insert((i, deadline), ret);
    ret
}
