use std::collections::HashMap;
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let mut index_map: HashMap<String, usize> = HashMap::new();
    loop {
        let _ = stdin.read_line(&mut buf);
        let c: usize = buf.trim().parse().unwrap();
        if c == 0 {return}
        buf.clear();

        let _ = stdin.read_line(&mut buf);
        for (i, cur) in buf.split_whitespace().enumerate() {
            index_map.insert(cur.to_string(), i);
        }
        buf.clear();


        let _ = stdin.read_line(&mut buf);
        let r: u16 = buf.trim().parse().unwrap();
        buf.clear();
        let mut dist = vec![vec![f32::MAX; c]; c];
        for _ in 0..r {
            let _ = stdin.read_line(&mut buf);
            let mut foo = buf.split_whitespace();
            let c1 = index_map[foo.next().unwrap()];
            let c2 = index_map[foo.next().unwrap()];

            let mut rate = foo.next().unwrap().split(":");
            let r1: f32 = rate.next().unwrap().parse().unwrap();
            let r2: f32 = rate.next().unwrap().parse().unwrap();
            let w = (r1/r2).log2();
            dist[c1][c2] = w;
            buf.clear();
        }

        let mut cont = true;
        for k in 0..c {
            for j in 0..c {
                for i in 0..c {
                    let val = dist[i][k] + dist[k][j];
                    if dist[i][j] > val {
                        dist[i][j] = val;
                        if i == j && val < 0.0 {
                            cont = false;
                            break;
                        }
                    }
                }
                if !cont{break}
            }
            if !cont{break}
        }
        if cont {println!("Ok")}
        else {println!("Arbitrage")}
    }
}


// use std::collections::{HashMap, HashSet};

// fn bellman_ford(
//     s: usize, 
//     c: &usize, 
//     g: &Vec<Vec<(usize, f32)>>,
//     candidates: &mut HashSet<usize>
// ) -> bool {
//     let mut dist = HashMap::new();
//     for v in 0..*c {
//         dist.insert(v, f32::MAX);
//     }
//     let mut pred = HashMap::new();
//     dist.insert(s, 0.0);
//     for _ in 0..*c-1 {
//         for parent in 0..*c {
//             for (child, w) in &g[parent] {
//                 if dist[child] > dist[&parent] + w {
//                     dist.insert(*child, dist[&parent]+w);
//                     pred.insert(*child, parent);
//                 }
//             }
//         }
//     }
//     for parent in 0..*c {
//         if dist[&parent] < f32::MAX {
//             candidates.remove(&parent);
//         }
//         for (child, w) in &g[parent] {
//             if dist[child] > dist[&parent] + w {
//                 return true;
//             }
//         }
//     }
//     return false;
    
// }

// fn main() {
//     let stdin = std::io::stdin();
//     let mut buf = String::new();
//     let mut index_map: HashMap<String, usize> = HashMap::new();
//     loop {
//         let _ = stdin.read_line(&mut buf);
//         let c: usize = buf.trim().parse().unwrap();
//         if c == 0 {return}
//         buf.clear();
//         let mut candidates: HashSet<usize> = HashSet::new();

//         let _ = stdin.read_line(&mut buf);
//         for (i, cur) in buf.split_whitespace().enumerate() {
//             index_map.insert(cur.to_string(), i);
//             candidates.insert(i);
//         }
//         buf.clear();

//         let _ = stdin.read_line(&mut buf);
//         let r: u16 = buf.trim().parse().unwrap();
//         buf.clear();
//         let mut g: Vec<Vec<(usize, f32)>> = vec![Vec::new(); c];
//         for _ in 0..r {
//             let _ = stdin.read_line(&mut buf);
//             let mut foo = buf.split_whitespace();
//             let c1 = index_map[foo.next().unwrap()];
//             let c2 = index_map[foo.next().unwrap()];

//             let mut rate = foo.next().unwrap().split(":");
//             let r1: f32 = rate.next().unwrap().parse().unwrap();
//             let r2: f32 = rate.next().unwrap().parse().unwrap();
//             let w = (r1/r2).log2();
//             g[c1].push((c2, w));
//             buf.clear();
//         }

//         let mut ok = true;
//         while candidates.len() > 0 {
//             if bellman_ford(*candidates.iter().next().unwrap(), &c, &g, &mut candidates) {
//                 ok = false;
//                 break
//             }
//         }
//         if ok {println!("Ok")}
//         else {println!("Arbitrage")}
//     }
// }