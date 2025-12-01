use std::collections::{BinaryHeap, HashMap, HashSet};

const DELTAS: [(i32, i32); 4] = [(0, 1), (-1, 0), (0, -1), (1, 0)];

struct Data {
    cost: i32,
    paths: HashSet<(i32, i32, usize)>,
}

impl Data {
    fn new() -> Self {
        Data {
            cost: i32::MAX,
            paths: HashSet::new(),
        }
    }
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

fn add_paths(
    i: i32,
    j: i32,
    dir: usize,
    prev: &HashMap<(i32, i32, usize), Data>,
    fast_tiles: &mut HashSet<(i32, i32)>,
) {
    fast_tiles.insert((i, j));
    if let Some(data) = prev.get(&(i, j, dir)) {
        for (x, y, k) in data.paths.iter() {
            add_paths(*x, *y, *k, prev, fast_tiles);
        }
    }
}

fn main() {
    let grid: Vec<Vec<char>> = std::io::stdin()
        .lines()
        .map(|x| x.unwrap().chars().collect())
        .collect();
    let (i, j) = get_symbol_coords(&grid, 'S');
    let mut pq = BinaryHeap::from([(0, i, j, 0)]);
    let mut prev: HashMap<(i32, i32, usize), Data> = HashMap::new();
    prev.insert(
        (i, j, 0),
        Data {
            cost: 0,
            paths: HashSet::new(),
        },
    );
    let mut fast_tiles = HashSet::new();
    let mut target_dist = i32::MAX;

    while let Some((c, i, j, dir)) = pq.pop() {
        let c = -c;
        let cur_cost = prev.get(&(i, j, dir)).unwrap().cost;
        if cur_cost < c {
            continue;
        }

        if grid[i as usize][j as usize] == 'E' {
            if c > target_dist {
                break;
            }
            add_paths(i, j, dir, &prev, &mut fast_tiles);
            target_dist = c;
            continue;
        }
        for k in 0..DELTAS.len() {
            let (x, y, new_cost) = {
                if k == dir {
                    let (di, dj) = DELTAS[k];
                    (i + di, j + dj, c + 1)
                } else {
                    let rotation = {
                        if (k as i32 - dir as i32).abs() == 2 {
                            2
                        } else {
                            1
                        }
                    };
                    (i, j, c + rotation * 1000)
                }
            };
            if grid[x as usize][y as usize] != '#' {
                let mem = prev.entry((x, y, k)).or_insert(Data::new());
                if new_cost > mem.cost {
                    continue;
                }
                if new_cost < mem.cost {
                    mem.paths.clear();
                }
                mem.cost = new_cost;
                if !mem.paths.insert((i, j, dir)) {
                    continue;
                }
                pq.push((-new_cost, x, y, k));
            }
        }
    }
    println!("{}", fast_tiles.len());
}
