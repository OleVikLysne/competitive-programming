use std::collections::HashSet;

// const ROWS: i64 = 7;
// const COLS: i64 = 11;
const ROWS: i64 = 103;
const COLS: i64 = 101;
const DELTAS: [(i64, i64); 8] = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)];

fn search(i: i64, j: i64, visited: &mut HashSet<(i64, i64)>, grid: &[[i32; COLS as usize]; ROWS as usize]) -> i32 {
    let mut stack = vec![(i, j)];
    let mut count = grid[i as usize][j as usize];
    while let Some((i, j)) = stack.pop() {
        for (di, dj) in DELTAS {
            let (x, y) = (i+di, j+dj);
            let x = x.rem_euclid(ROWS);
            let y = y.rem_euclid(COLS);
            if grid[x as usize][y as usize] > 0 && visited.insert((x, y)) {
                count += grid[x as usize][y as usize];
                stack.push((x, y));
            }
        }
    }
    return count
}



fn main() {
    let mut grid = [[0; COLS as usize]; ROWS as usize];
    let mut robots = Vec::new();

    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut line_split = line.split_ascii_whitespace();
        let left = line_split.next().unwrap().trim_start_matches("p=");
        let right = line_split.next().unwrap().trim_start_matches("v=");

        let left: Vec<i64> = left.split(",").map(|x| x.parse().unwrap()).collect();
        let right: Vec<i64> = right.split(",").map(|x| x.parse().unwrap()).collect();
        let (i, j) = (left[1], left[0]);
        let (di, dj) = (right[1], right[0]);
        robots.push((i, j, di, dj));
        grid[i as usize][j as usize] += 1;
    }

    for steps in 0.. {
        println!("{}", steps);
        let mut visited = HashSet::new();
        for (i, j, _, _) in robots.iter() {
            if visited.insert((*i, *j)) {
                let count = search(*i, *j, &mut visited, &grid);
                if count > (robots.len() / 3) as i32 {
                    return
                }
            }
        }
        for (i, j, di, dj)in robots.iter_mut() {
            grid[*i as usize][*j as usize] -= 1;
            *i += *di;
            *j += *dj;
            *i = i.rem_euclid(ROWS);
            *j = j.rem_euclid(COLS);
            grid[*i as usize][*j as usize] += 1;
        }
    }
}
