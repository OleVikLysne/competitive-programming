const DELTAS: [(isize, isize); 8] = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)];
const PATTERN: [char; 4] = ['X', 'M', 'A', 'S'];

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
            for (di, dj) in DELTAS {
                let mut count = 0;
                let mut x = i;
                let mut y = j;
                while count < 4 && 0 <= x && x < rows && 0 <= y && y < cols {

                    if PATTERN[count] != grid[x as usize][y as usize] {
                        break
                    }
                    count += 1;
                    x += di;
                    y += dj;
                }
                if count == 4 {
                    total += 1;
                }
            }
        }
    }
    println!("{}", total);
}
