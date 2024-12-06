use std::collections::HashSet;

const DELTAS: [(isize, isize); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

fn valid(i: isize, j: isize, rows: usize, cols: usize) -> bool {
    return i >= 0 && i < rows as isize && j >= 0 && j < cols as isize
}

fn loop_check(mut i: isize, mut j: isize, mut dir: usize, grid: &Vec<Vec<char>>) -> bool {
    let mut visited = HashSet::new();
    let rows = grid.len();
    let cols = grid[0].len();
    loop {
        if !visited.insert((i, j, dir)) {
            return true
        }
        let (di, dj) = DELTAS[dir];
        let x = i+di;
        let y = j+dj;
        if !valid(x, y, rows, cols) {break}
        if grid[x as usize][y as usize] == '#' {
            dir = (dir + 1) % 4;
        } else {
            (i, j) = (x, y);
        }

    }
    false
}

fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let row: Vec<char> = line.chars().collect();
        grid.push(row);
    }
    let rows = grid.len();
    let cols = grid[0].len();
    let mut start = (0, 0);
    let mut found= false;
    for i in 0..rows {
        for j in 0..cols {
            if grid[i][j] == '^' {
                start = (i as isize, j as isize);
                found = true;
                break
            }
        }
        if found { break }
    }

    let mut dir = 0;
    let (mut i, mut j) = start;
    let mut visited = HashSet::new();
    let mut blocks = HashSet::new();

    loop {
        visited.insert((i, j));
        let (di, dj) = DELTAS[dir];
        let x = i+di;
        let y = j+dj;
        if !valid(x, y, rows, cols) {
            break
        }
        if grid[x as usize][y as usize] == '#' {
            dir = (dir+1) % 4;
            continue
        } 

        if !blocks.contains(&(x, y)) {
            grid[x as usize][y as usize] = '#';
            if loop_check(start.0, start.1, 0, &grid) {
                blocks.insert((x, y));
            }
            grid[x as usize][y as usize] = '.';
        }
        (i, j) = (x, y);

    }
    println!("{}", blocks.len());
}