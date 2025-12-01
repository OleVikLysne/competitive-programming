use std::collections::{HashMap, HashSet};

const DELTAS: [(i32, i32); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];

fn get_start(grid: &[Vec<char>]) -> (i32, i32) {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == '@' {
                return (i as i32, j as i32);
            }
        }
    }
    return (0, 0);
}

fn box_search(grid: &[Vec<char>], i: i32, j: i32, k: usize) -> Option<HashSet<(i32, i32)>> {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut stack = vec![(i, j)];

    let (di, dj) = DELTAS[k];
    while let Some((i, j)) = stack.pop() {
        let (x, y) = (i + di, j + dj);
        if grid[x as usize][y as usize] == '#' {
            return None;
        }
        if grid[x as usize][y as usize] == '.' {
            continue;
        }

        if visited.insert((x, y)) {
            stack.push((x, y));
        }

        if k % 2 == 1 {
            if grid[x as usize][y as usize] == '[' {
                if visited.insert((x, y + 1)) {
                    stack.push((x, y + 1))
                }
            } else {
                if visited.insert((x, y - 1)) {
                    stack.push((x, y - 1))
                }
            }
        }
    }
    return Some(visited)
}

fn solve(moves: &[char], grid: &mut [Vec<char>]) -> u64 {
    let move_map = HashMap::from([
        ('>', 0),
        ('^', 1),
        ('<', 2),
        ('v', 3)
    ]);
    let (mut i, mut j) = get_start(grid);
    grid[i as usize][j as usize] = '.';
    for dir in moves {
        let k = *move_map.get(dir).unwrap();
        let (di, dj) = DELTAS[k];
        let (x, y) = (i + di, j + dj);
        if grid[x as usize][y as usize] == '#' {
            continue;
        }

        if grid[x as usize][y as usize] == '.' {
            (i, j) = (x, y);
            continue;
        }
        if let Some(visited) = box_search(&grid, i, j, k) {
            let mut visited: Vec<(i32, i32)> = visited.into_iter().collect();
            visited.sort_by_key(|(x, y)| (-*x * di, -*y * dj));
            for (a, b) in visited {
                grid[(a + di) as usize][(b + dj) as usize] = grid[a as usize][b as usize];
                grid[a as usize][b as usize] = '.';
            }
            (i, j) = (x, y)
        }
    }

    let mut total = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == '[' {
                total += (i * 100 + j) as u64;
            }
        }
    }
    for row in grid {
        println!("{}", row.iter().collect::<String>())
    }
    return total;
}

fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    let extension_map = HashMap::from([
        ('#', "##"),
        ('O', "[]"),
        ('.', ".."),
        ('@', "@.")
    ]);
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        if line == "" {
            break
        }
        let mut l = Vec::new();
        for char in line.chars() {
            l.extend(extension_map.get(&char).unwrap().chars());
        }
        grid.push(l);
    }

    let mut moves: Vec<char> = Vec::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        moves.extend(line.chars());
    }
    println!("{}", solve(&moves, &mut grid))
}
