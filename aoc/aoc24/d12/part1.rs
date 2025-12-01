use std::collections::VecDeque;

const DELTAS: [(isize, isize); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

fn valid(i: isize, j: isize, grid: &Vec<Vec<char>>) -> bool {
    return 0 <= i && i < grid.len() as isize && 0 <= j && j < grid[0].len() as isize
}


fn search(i: usize, j: usize, grid: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) -> u32 {
    visited[i][j] = true;
    let mut perim = 0;
    let mut area = 1;
    let mut q = VecDeque::from([(i as isize, j as isize)]);
    while let Some((i, j)) = q.pop_front() {
        for (di, dj) in DELTAS {
            let (x, y) = (i+di, j+dj);
            if !valid(x, y, grid) || grid[i as usize][j as usize] != grid[x as usize][y as usize] {
                perim += 1;
                continue
            }

            if !visited[x as usize][y as usize] {
                area += 1;
                q.push_back((x, y));
                visited[x as usize][y as usize] = true;
            } 
        }

    }
    return area*perim
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
                total += search(i, j, &grid, &mut visited);
            }
        }
    }
    println!("{}", total);
}
