use std::collections::{HashSet, VecDeque};

const DELTAS: [(isize, isize); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];

fn valid(i: isize, j: isize, grid: &Vec<Vec<char>>) -> bool {
    return 0 <= i && i < grid.len() as isize && 0 <= j && j < grid[0].len() as isize
}

fn next_pos(i: usize, j: usize, k: usize, grid:&Vec<Vec<char>>) -> Option<(usize, usize)> {
    let (i, j) = (i as isize, j as isize);
    let (di, dj) = DELTAS[k];
    let (x, y) = (i+di, j+dj);
    if valid(x, y, grid) {
        return Some((x as usize, y as usize))
    }
    return None
}


fn fence_cost(i: usize, j: usize,  grid: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) -> u32 {
    visited[i][j] = true;
    let mut counted = HashSet::new();
    let mut sides = 0;
    let mut area = 0;
    let mut q = VecDeque::from([(i, j)]);
    while let Some((i, j)) = q.pop_front() {
        area += 1;
        for k in 0..4 {
            if let Some((x, y)) = next_pos(i, j, k, grid) {
                if grid[i][j] == grid[x][y] {
                    if !visited[x][y] {
                        q.push_back((x, y));
                        visited[x][y] = true;
                    }
                    continue
                }
            }
            if counted.insert((i, j, k)) {
                sides += 1;
                for z in [(k+1) % 4, (k+3) % 4] {
                    let (mut a_prev, mut b_prev) = (i, j);
                    while let Some((a, b)) = next_pos(a_prev, b_prev, z, grid) {
                        if grid[i][j] != grid[a][b] {
                            break
                        }
                        if let Some((q, w)) = next_pos(a, b, k, grid) {
                            if grid[q][w] == grid[i][j] {
                                break
                            }
                        }
                        counted.insert((a, b, k));
                        (a_prev, b_prev) = (a, b);

                    }
                }
            }
        }
    }
    return sides*area
}


fn main() {
    let grid: Vec<Vec<char>> = std::io::stdin()
        .lines()
        .map(|x| x.unwrap().chars().collect())
        .collect();

    let rows = grid.len();
    let cols = grid[0].len();
    let mut visited = vec![vec![false; cols]; rows];
    let mut total = 0;
    for i in 0..rows {
        for j in 0..cols {
            if !visited[i][j] {
                let f = fence_cost(i, j, &grid, &mut visited);
                total += f
            }
        }
    }
    println!("{}", total);
}
