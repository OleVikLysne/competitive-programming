use std::collections::{HashMap, HashSet};
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut foo = buf.split_whitespace();
    let w: usize = foo.next().unwrap().parse().unwrap();
    let p: usize = foo.next().unwrap().parse().unwrap();
    let mut W = Vec::with_capacity(w);
    for _ in 0..w {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf
                    .split_whitespace()
                    .map(|x| x.parse::<i32>().unwrap());
        let pos = (foo.next().unwrap(), foo.next().unwrap());
        W.push(pos);
    }
    let mut lines = Vec::with_capacity(p);
    let mut to_visit = HashSet::new();
    let mut g = vec![Vec::new(); p];
    for j in 0..p {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace();
        let i: usize = foo.next().unwrap().parse().unwrap();
        let x2: i32 = foo.next().unwrap().parse().unwrap();
        let y2: i32 = foo.next().unwrap().parse().unwrap();
        let line = (W[i-1], (x2, y2));

        for (k, l) in lines.iter().enumerate() {
            if intersect(l, &line) {
                g[j].push(k);
                g[k].push(j);
                to_visit.insert(k);
            }
        }
        lines.push(line);
    }

    let mut colors: HashMap<usize, i8> = HashMap::new();
    while to_visit.len() > 0 {
        let s = to_visit.iter().next().unwrap().clone();
        if !bipartite(&g, &mut colors, &mut to_visit, s, 0) {
            println!("impossible");
            return
        }
    }
    println!("possible")
}

fn bipartite(
    g: &Vec<Vec<usize>>, 
    colors: &mut HashMap<usize, i8>,
    to_visit: &mut HashSet<usize>,
    s: usize, 
    color: i8
) -> bool {

    match colors.get(&s) {
        Some(c) => {
            if *c != color { return false }
            return true
        },
        None => {colors.insert(s, color)}
    };
    to_visit.remove(&s);
    let next_color = (color + 1) % 2;
    for child in &g[s] {
        if !bipartite(g, colors, to_visit, *child, next_color) {
            return false
        }
    }
    true
}

fn cross(v1: &(i32, i32), v2: &(i32, i32)) -> i32 {
    return v1.0 * v2.1 - v1.1 * v2.0;
}

fn orient(v1: &(i32, i32), v2: &(i32, i32), v3: &(i32, i32)) -> i32 {
    let foo = (v2.0-v1.0, v2.1-v1.1);
    let bar = (v3.0-v1.0, v3.1-v1.1);
    return cross(&foo, &bar);
}

fn intersect(line1: &((i32, i32), (i32, i32)), line2: &((i32, i32), (i32, i32))) -> bool {
    let a = &line1.0;
    let b = &line1.1;
    let c = &line2.0;
    let d = &line2.1;
    if b == d { return true }
    let oa = orient(c,d,a);
    let ob = orient(c,d,b);
    let oc = orient(a,b,c);
    let od = orient(a,b,d);
    if ((oa < 0 && ob > 0) || (oa > 0 && ob < 0)) && ((oc < 0 && od > 0) || oc > 0 && od < 0) {
        return true;
    }
    false
}