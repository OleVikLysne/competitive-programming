use std::collections::{HashMap, HashSet};

fn main() {
    let mut g = HashMap::new();

    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let (a, b) = line.split_once("-").unwrap();
        let a = a.to_string();
        let b = b.to_string();
        g.entry(a.clone()).or_insert(Vec::new()).push(b.clone());
        g.entry(b).or_insert(Vec::new()).push(a);
    }
    let mut cycles = HashSet::new();
    for v in g.keys() {
        if v.chars().next().unwrap() != 't' {continue}
        for u in g.get(v).unwrap().iter() {
            let z = g.get(u).unwrap();
            for w in g.get(v).unwrap().iter() {
                if u == w {continue}
                if z.contains(w) {
                    let mut vector = vec![v.clone(), u.clone(), w.clone()];
                    vector.sort();
                    cycles.insert(vector);
                }
            }
        }
    }
    println!("{}", cycles.len());
}