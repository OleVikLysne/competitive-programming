use std::collections::VecDeque;

const SIZE: usize = 71;
type Grid = [[bool; SIZE]; SIZE];
type C = i32;

const DELTAS: [(C, C); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];
const START: (C, C) = (0, 0);
const TARGET: (C, C) = (SIZE as C - 1, SIZE as C - 1);

fn valid(i: &C, j: &C, grid: &Grid) -> bool {
    return 0 <= *i && *i < grid.len() as C && 0 <= *j && *j < grid[0].len() as C;
}

fn moves(i: C, j: C) -> impl Iterator<Item = (C, C)> {
    return DELTAS.iter().map(move |(di, dj)| (i + *di, j + *dj));
}

fn valid_moves(i: C, j: C, grid: &Grid) -> impl Iterator<Item = (usize, usize)> + '_ {
    return moves(i, j)
        .filter(|(i, j)| valid(i, j, grid))
        .map(|(i, j)| (i as usize, j as usize));
}


fn run(steps: usize, coords: &Vec<Vec<C>>) -> bool {
    let mut grid = [[false; SIZE]; SIZE];
    for coord in &coords[..steps] {
        let (i, j) = (coord[1], coord[0]);
        grid[i as usize][j as usize] = true;
    }
    let mut visited = [[false; SIZE]; SIZE];
    let (i, j) = START;
    visited[i as usize][j as usize] = true;
    let mut q = VecDeque::from([START]);
    while let Some((i, j)) = q.pop_front() {
        if (i, j) == TARGET {
            return true
        }
        for (x, y) in valid_moves(i, j, &grid) {
            if !grid[x][y] && !visited[x][y] {
                visited[x][y] = true;
                q.push_back((x as C, y as C));
            }
        }
    }
    return false
}

fn main() {
    let coords: Vec<Vec<C>> = std::io::stdin()
        .lines()
        .map(|x| {
            x.unwrap()
                .split(",")
                .into_iter()
                .map(|x| x.parse::<C>().unwrap())
                .collect()
        })
        .collect();

    let (mut lower, mut upper) = (0, coords.len());
    while lower < upper {
        let mid = lower + (upper-lower)/2;
        if run(mid, &coords) {
            lower = mid + 1;
        } else {
            upper = mid;
        }
    }
    println!("{:?}", coords[lower-1]);
}
