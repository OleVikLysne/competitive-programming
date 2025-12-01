use std::collections::{VecDeque, HashSet};

type C = i32;
const DELTAS: [(C, C); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];

fn valid<T>(i: &C, j: &C, grid: &[Vec<T>]) -> bool {
    return 0 <= *i && *i < grid.len() as C && 0 <= *j && *j < grid[0].len() as C;
}

fn moves(i: C, j: C) -> impl Iterator<Item = (C, C)> {
    return DELTAS.iter().map(move |(di, dj)| (i + di, j + dj));
}

fn valid_moves<T>(i: C, j: C, grid: &[Vec<T>]) -> impl Iterator<Item = (usize, usize)> + '_ {
    return moves(i, j)
        .filter(move |(i, j)| valid(i, j, grid))
        .map(|(i, j)| (i as usize, j as usize));
}

fn valid_20_moves(i: C, j: C, grid: &[Vec<char>]) -> Vec<(C, C)> {
    let mut res = Vec::new();
    let mut q = VecDeque::from([(i, j, 0)]);
    let mut visited = HashSet::from([(i as usize, j as usize)]);
    while let Some((i, j, c)) = q.pop_front() {
        for (x, y) in valid_moves(i, j, grid) {
            if visited.insert((x, y)) {
                if c+1 < 20 {
                    q.push_back((x as C, y as C, c+1));
                }
                if grid[x][y] != '#' {
                    res.push((x as C, y as C));
                }
            }  
        }
    }
    return res
}

fn get_symbol_coords(grid: &[Vec<char>], target: char) -> (C, C) {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == target {
                return (i as C, j as C);
            }
        }
    }
    return (0, 0);
}

fn get_dist(grid: &[Vec<char>]) -> Vec<Vec<C>> {
    let (i, j) = get_symbol_coords(&grid, 'E');
    let rows = grid.len();
    let cols = grid[0].len();
    let inf = C::MAX;
    let mut dist = vec![vec![inf; cols]; rows];
    dist[i as usize][j as usize] = 0;
    let mut q = VecDeque::from([(i, j, 0)]);
    while let Some((i, j, c)) = q.pop_front() {
        for (x, y) in valid_moves(i, j, grid) {
            if grid[x][y] != '#' && dist[x][y] == inf {
                dist[x][y] = c+1;
                q.push_back((x as C, y as C, c+1));
            }
        }
    }
    return dist
}

fn manhattan_dist(i: C, j: C, x: C, y: C) -> C {
    return (i-x).abs() + (j-y).abs()
}

fn solve(grid: &[Vec<char>], dist: &[Vec<C>]) -> u32 {
    let mut res = 0;
    let (i, j) = get_symbol_coords(grid, 'S');

    let rows = grid.len();
    let cols = grid[0].len();
    let mut visited = vec![vec![false; cols]; rows];
    visited[i as usize][j as usize] = true;

    let mut stack = vec![(i, j)];
    while let Some((i, j)) = stack.pop() {
        for (x, y) in valid_20_moves(i, j, grid) {
            if dist[x as usize][y as usize] <= dist[i as usize][j as usize] - 100 - manhattan_dist(i, j, x, y)  {
                res += 1;
            }
        }
        for (x, y) in valid_moves(i, j, grid) {
            if grid[x][y] == '#' {continue}
            if !visited[x][y] {
                visited[x][y] = true;
                stack.push((x as C, y as C));
            }
        }
    }
    return res
}

fn main() {
    let grid: Vec<Vec<char>> = std::io::stdin()
        .lines()
        .map(|x| x.unwrap().chars().collect())
        .collect();
    let dist = get_dist(&grid);
    println!("{}", solve(&grid, &dist));
}
