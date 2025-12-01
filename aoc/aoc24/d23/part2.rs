use std::collections::{HashMap, HashSet};

fn dfs(v: &String, g: &HashMap<String, HashSet<String>>, path: &mut HashSet<String>, tried: &mut HashSet<Vec<String>>) {
    let neighbours = g.get(v).unwrap();
    if path.intersection(neighbours).count() != path.len() {
        return
    }
    path.insert(v.clone());
    let mut path_vec: Vec<String> = path.iter().map(|x| x.clone()).collect();
    path_vec.sort();
    if !tried.insert(path_vec) {
        path.remove(v);
        return
    }
    for u in neighbours.iter() {
        if !path.contains(u) {
            dfs(u, g, path, tried);
        }
    }
    path.remove(v);
}

fn main() {
    let mut g = HashMap::new();

    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let (a, b) = line.split_once("-").unwrap();
        let a = a.to_string();
        let b = b.to_string();
        g.entry(a.clone()).or_insert(HashSet::new()).insert(b.clone());
        g.entry(b).or_insert(HashSet::new()).insert(a);
    }
    let mut tried = HashSet::new();
    for v in g.keys() {
        println!("{}", v);
        dfs(v, &g, &mut HashSet::new(), &mut tried);
    }
    let best = tried.iter().max_by_key(|x| x.len()).unwrap();
    println!("{}", best.join(","));
}
