const DELTAS: [(isize, isize); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

fn search(i: isize, j: isize, grid: &[Vec<u8>]) -> usize {
    if grid[i as usize][j as usize] == 9 {
        return 1
    }
    let mut res = 0;
    for (di, dj) in DELTAS {
        let (x, y) = (i+di, j+dj);
        if 0 <= x && x < grid.len() as isize
        && 0 <= y && y < grid[0].len() as isize
        && grid[x as usize][y as usize] == grid[i as usize][j as usize] + 1 {
            res += search(x, y, grid);
        }
    }
    return res;
}

fn main() {
    let mut grid: Vec<Vec<u8>> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        grid.push(line.chars().map(|x| x as u8 - b'0').collect());
    }
    let rows = grid.len();
    let cols = grid[0].len();
    let mut res = 0;
    for i in 0..rows {
        for j in 0..cols {
            if grid[i][j] == 0 {
                res += search(i as isize, j as isize, &grid);
            }
        }
    }
    println!("{}", res);
}