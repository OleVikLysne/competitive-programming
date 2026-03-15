const N: usize = 2500;
use std::collections::HashMap;

fn main() {
    let mut edges: [[i32; N]; N] = [[0; N]; N];

    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut nm = buf.trim().split_ascii_whitespace();
    let n: usize = nm.next().unwrap().parse().unwrap();
    let m: usize = nm.next().unwrap().parse().unwrap();
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    let mut foo = buf.trim().split_ascii_whitespace();
    let mut intersections: Vec<(u32, u32)> = Vec::new();
    for _ in 0..n {
        let x: u32 = foo.next().unwrap().parse().unwrap();
        let y: u32 = foo.next().unwrap().parse().unwrap();
        intersections.push((x, y))
    }
    let mut g: Vec<[usize; 4]>  = vec![[usize::MAX; 4]; n];
    for _ in 0..m {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.trim().split_ascii_whitespace();
        let i: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
        let j: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
        let k: i32 = foo.next().unwrap().parse().unwrap();
        let d = get_dir(i, j, &intersections);
        g[i][d] = j;
        g[j][(d+2) % 4] = i;
        add_edge(i, j, k, &mut edges);
    }

    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut sd = buf.trim().split_ascii_whitespace();
    let s: usize = sd.next().unwrap().parse::<usize>().unwrap() - 1;
    let mut d: usize = {
        let d = sd.next().unwrap();
        if d == "E" {
            0
        } else if d == "N" {
            1
        } else if d == "W" {
            2
        } else {
            3
        }
    };

    let mut j = s;
    let mut i = g[j][d];
    decrement_edge(i, j, 1, &mut edges);
    let mut path = vec![(j, i)];
    let mut path_map: HashMap<(usize, usize), usize> = HashMap::new();
    path_map.insert((j, i), 0);

    loop {
        let moves = valid_moves(i, j, &g, &edges);
        let n = moves.len();
        if n == 0 {
            println!("{} {}", intersections[i].0, intersections[i].1);
            break
        }
        j = i;
        i = {
            if n == 1 {
                g[i][moves[0]]
            } else if n == 2 {
                let best_left = (d+1) % 4;
                if moves.contains(&best_left) {
                    g[i][best_left]
                } else {
                    g[i][d]
                }
            } else {
                g[i][d]
            }
        };
        d = get_dir(j, i, &intersections);
        decrement_edge(i, j, 1, &mut edges);
        let t = (j, i);
        if let Some(lb) = path_map.get(&t) {
            let mut min_val = i32::MAX;
            for z in *lb..path.len() {
                let (x, y) = &path[z];
                min_val = min_val.min(get_edge(*x, *y, &edges));
                if min_val <= 4 { break }
            }
            min_val -= 4;
            if min_val > 0 {
                for z in *lb..path.len() {
                    let (x, y) = &path[z];
                    decrement_edge(*x, *y, min_val, &mut edges)
                }
            }
            path_map.clear();
            path.clear();
        }
        path_map.insert(t, path.len());
        path.push(t);
    }

}

fn valid_moves(i: usize, prev_pos: usize, g: &Vec<[usize; 4]>, edges: & [[i32; N]; N]) -> Vec<usize> {
    let mut l: Vec<usize> = Vec::new();
    for (x, j) in g[i].iter().enumerate() {
        if *j != usize::MAX && *j != prev_pos && get_edge(i, *j, edges) > 0 {
            l.push(x);
        }
    }
    return l
}

fn get_dir(i: usize, j: usize, intersections: &[(u32, u32)]) -> usize {
    /*
    E = 0
    N = 1
    W = 2
    S = 3
     */
    let (x1, y1) = &intersections[i];
    let (x2, y2) = &intersections[j];
    return {
        if x1 == x2 {
            if y1 > y2 {
                3
            } else {
                1
            }
        } else {
            if x1 > x2 {
                2
            } else {
                0
            }
        }
    }
}

fn add_edge(mut i: usize, mut j: usize, k: i32, edges: &mut [[i32; N]; N]) {
    if i < j {
        std::mem::swap(&mut i,&mut  j);
    }
    edges[i][j] = k
}

fn get_edge(mut i: usize, mut j: usize, edges: & [[i32; N]; N]) -> i32 {
    if i < j {
        std::mem::swap(&mut i,&mut  j);
    }
    return edges[i][j]
}

fn decrement_edge(mut i: usize, mut j: usize, amount: i32, edges: &mut [[i32; N]; N]) {
    if i < j {
        std::mem::swap(&mut i,&mut  j);
    }
    edges[i][j] -= amount;
}

