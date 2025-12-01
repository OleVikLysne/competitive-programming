use std::collections::VecDeque;

const DELTAS: [(i32, i32); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];
type C = i32;

fn valid<T>(i: &C, j: &C, grid: &[Vec<T>]) -> bool {
    return 0 <= *i && *i < grid.len() as C && 0 <= *j && *j < grid[0].len() as C;
}

fn moves(i: C, j: C) -> impl Iterator<Item = (C, C)> {
    return DELTAS.into_iter().map(move |(di, dj)| (i + di, j + dj));
}

fn double_moves(i: C, j: C) -> impl Iterator<Item = (C, C)> {
    return DELTAS.into_iter().map(move |(di, dj)| (i + di*2, j + dj*2));
}

fn valid_moves<T>(i: C, j: C, grid: &[Vec<T>]) -> impl Iterator<Item = (usize, usize)> + '_ {
    return moves(i, j)
        .filter(|(i, j)| valid(i, j, grid))
        .map(|(i, j)| (i as usize, j as usize));
}

fn valid_double_moves<T>(i: C, j: C, grid: &[Vec<T>]) -> impl Iterator<Item = (usize, usize)> + '_ {
    return double_moves(i, j)
        .filter(|(i, j)| valid(i, j, grid))
        .map(|(i, j)| (i as usize, j as usize));
}

fn get_symbol_coords(grid: &[Vec<char>], target: char) -> (i32, i32) {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == target {
                return (i as i32, j as i32);
            }
        }
    }
    return (0, 0);
}

fn get_dist(grid: &[Vec<char>]) -> Vec<Vec<i32>> {
    let (i, j) = get_symbol_coords(&grid, 'E');
    let rows = grid.len();
    let cols = grid[0].len();
    let inf = i32::MAX-100;
    let mut dist = vec![vec![inf; cols]; rows];
    dist[i as usize][j as usize] = 0;
    let mut q = VecDeque::from([(i, j, 0)]);
    while let Some((i, j, c)) = q.pop_front() {
        for (x, y) in valid_moves(i, j, grid) {
            if grid[x][y] != '#' && dist[x][y] == inf {
                dist[x][y] = c+1;
                q.push_back((x as i32, y as i32, c+1));
            }
        }
    }
    return dist
}

fn solve(grid: &[Vec<char>], dist: &[Vec<i32>]) -> u32 {
    let mut res = 0;
    let (i, j) = get_symbol_coords(grid, 'S');

    let rows = grid.len();
    let cols = grid[0].len();
    let mut visited = vec![vec![false; cols]; rows];
    visited[i as usize][j as usize] = true;

    let mut stack = vec![(i, j)];
    while let Some((i, j)) = stack.pop() {
        for (x, y) in valid_double_moves(i, j, grid) {
            if grid[x][y] == '#' {continue}
            if dist[x][y] <= dist[i as usize][j as usize]-102  {
                res += 1;
            }
        }
        for (x, y) in valid_moves(i, j, grid) {
            if grid[x][y] == '#' {continue}
            if !visited[x][y] {
                visited[x][y] = true;
                stack.push((x as i32, y as i32));
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
