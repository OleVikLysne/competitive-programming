const DELTAS: [(i32, i32); 8] = [
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
];

const DELTAS: [(i32, i32); 4] = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
];

fn valid(i: &i32, j: &i32, grid: &[Vec<i32>]) -> bool {
    return 0 <= *i && *i < grid.len() as i32 && 0 <= *j && *j < grid[0].len() as i32
}

fn moves(
    i: i32,
    j: i32,
) -> impl Iterator<Item = (i32, i32)> {
    return DELTAS.iter()
                .map(move |(di, dj)| (i+*di, j+*dj))
}

fn valid_moves(
    i: i32,
    j: i32,
    grid: &[Vec<i32>],
) -> impl Iterator<Item = (i32, i32)> + '_ {
    return moves(i, j).filter(|(i, j)| valid(i, j, grid))
}