type C = i32;

const DELTAS: [(C, C); 4] = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
];
const DELTAS: [(C, C); 8] = [
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
];

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