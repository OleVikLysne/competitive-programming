use std::collections::{HashSet, HashMap};
fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        grid.push(line.chars().collect());
    }
    let rows = grid.len();
    let cols = grid[0].len();
    let mut map = HashMap::new();
    for i in 0..rows {
        for j in 0..cols {
            let c = grid[i][j];
            if c == '.' {continue}
            map.entry(c).or_insert(Vec::new()).push((i as isize, j as isize));
        }
    }
    let mut anti_nodes = HashSet::new();
    for vec in map.values() {
        for (k, (i, j)) in vec.iter().enumerate() {
            for (x, y) in &vec[k+1..] {
                let dx = *i-*x;
                let dy = *j-*y;
                for (mut a, mut b, da, db) in [(*x, *y, dx, dy), (*i, *j, -dx, -dy)] {
                    loop {
                        a += da;
                        b += db;
                        if 0 <= a && a < rows as isize && 0 <= b && b < cols as isize {
                            anti_nodes.insert((a, b));
                        } else {break}
                    }
                }
            }
        }
    }
    println!("{}", anti_nodes.len());
}