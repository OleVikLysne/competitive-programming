use std::collections::HashSet;

fn main() {
    let stdin = std::io::stdin();
    let mut g = vec![HashSet::new(); 100];
    let mut buf = String::new();
    loop {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        if buf.trim().len() == 0 {
            break
        }
        let mut foo = buf.trim().split("|");
        let v: usize = foo.next().unwrap().parse().unwrap();
        let u: usize = foo.next().unwrap().parse().unwrap();
        g[v].insert(u);
    }

    
    let mut total = 0;
    for line in stdin.lines() {
        let line = line.unwrap();
        let arr: Vec<usize> = line.split(",").map(|x| x.parse::<usize>().unwrap()).collect();
        let mut valid = true;
        for i in 1..arr.len() {
            if !g[arr[i-1]].contains(&arr[i]) {
                valid = false;
                break
            }
        }
        if valid {
            total += arr[arr.len()/2]
        }
    }
    println!("{}", total);
}
