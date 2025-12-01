use std::collections::HashMap;

fn get_start(grid: &[Vec<char>]) -> (i32, i32) {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == '@' {
                return (i as i32, j as i32)
            }
        }
    }
    return (0, 0)
}


fn solve(moves: &[char], grid: &mut [Vec<char>]) -> u64 {
    let move_map = HashMap::from([
        ('>', (0, 1)),
        ('^', (-1, 0)),
        ('<', (0, -1)),
        ('v', (1, 0))
    ]);
    let (mut i, mut j) = get_start(grid);
    for dir in moves {
        let (di, dj) = move_map.get(dir).unwrap();
        let (mut x, mut y) = (i+*di, j+*dj);
        let (a, b) = (x, y);
        while grid[x as usize][y as usize] == 'O'  {
            x += *di;
            y += *dj;
        }
        if grid[x as usize][y as usize] == '#' {continue}
        grid[x as usize][y as usize] = grid[a as usize][b as usize];
        grid[a as usize][b as usize] = grid[i as usize][j as usize];
        grid[i as usize][j as usize] = '.';
        (i, j) = (a, b);
    }

    let mut total = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 'O' {
                total += (i*100+j) as u64;
            }
        }
    }
    return total
}


fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        if line == "" {
            break
        }
        grid.push(line.chars().collect());
    }
    
    let mut moves: Vec<char> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        moves.extend(line.chars());
    }
    println!("{}", solve(&moves, &mut grid));
}
