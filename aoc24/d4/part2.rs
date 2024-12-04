const DELTAS: [(isize, isize); 2] = [(1, 1), (-1, 1)];

fn valid(i: isize, j: isize, rows: isize, cols: isize) -> bool {
    return 0 <= i && i < rows && 0 <= j && j < cols
}
fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        grid.push(line.chars().collect());
    }

    let mut total = 0;

    let rows = grid.len() as isize;
    let cols = grid[0].len() as isize;
    for i in 0..rows {
        for j in 0..cols {
            if grid[i as usize][j as usize] != 'A' {
                continue
            }
            let mut dummy = true;
            for (di, dj) in DELTAS {
                let (x, y, k, l) = (i+di, j+dj, i-di, j-dj);
                if !valid(x, y, rows, cols) || !valid(k, l, rows, cols) {
                    dummy = false;
                    break;
                }
                let a = grid[x as usize][y as usize];
                let b = grid[k as usize][l as usize];
                if !( (a == 'M' && b == 'S') || (a == 'S' && b == 'M') ) {
                    dummy = false;
                    break
                }
            }
            if dummy {
                total += 1;
            }
        }
    }
    println!("{}", total);
}
