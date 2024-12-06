use std::collections::HashSet;

const DELTAS: [(isize, isize); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

fn main() {
    let mut grid = Vec::new();
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
    loop {
        visited.insert((i, j));
        let (di, dj) = DELTAS[dir];
        let x = i+di;
        let y = j+dj;
        if x < 0 || x >= rows as isize || y < 0 || y >= cols as isize {
            break
        }
        if grid[x as usize][y as usize] == '#' {
            dir = (dir+1) % 4;
            continue
        }
        (i, j) = (x, y);
    }
    println!("{}", visited.len());

}