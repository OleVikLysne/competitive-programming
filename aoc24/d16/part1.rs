use std::collections::{BinaryHeap, HashSet};

const DELTAS: [(i32, i32); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];

fn get_start(grid: &[Vec<char>]) -> (i32, i32) {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 'S' {
                return (i as i32, j as i32);
            }
        }
    }
    return (0, 0);
}

fn main() {
    let grid: Vec<Vec<char>> = std::io::stdin().lines().map(|x| x.unwrap().chars().collect()).collect();
    let (i, j) = get_start(&grid);
    let mut pq = BinaryHeap::from([(0, i, j, 0)]);
    let mut visited: HashSet<(i32, i32, usize)> = HashSet::new();
    while let Some((c, i, j, dir)) = pq.pop() {
        if !visited.insert((i, j, dir)) {
            continue
        }
        let c = -c;
        if grid[i as usize][j as usize] == 'E' {
            println!("{}", c);
            return
        }
        for k in 0..DELTAS.len() {
            if k == dir {
                let (di, dj) = DELTAS[k];
                let (x, y) = (i+di, j+dj);
                if grid[x as usize][y as usize] != '#' && !visited.contains(&(x, y, k)) {
                    pq.push((-(c+1), x, y, k));
                }
            } else {
                if !visited.contains(&(i, j, k)) {
                    let rotation = {
                        if (k as i32 - dir as i32).abs() == 2 {
                            2
                        } else {
                            1
                        }
                    };
                    let new_cost = c + rotation*1000;
                    pq.push((-new_cost, i, j, k));
                }
            }
        }

    }

}