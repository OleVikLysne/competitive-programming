use std::collections::HashMap;

const ROBOTS: usize = 26;

type C = i32;
type Grid = [[char; 3]; 4];
type State = [(C, C); ROBOTS-1];

const NUMPAD: Grid = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A'],
];

const DIRPAD: Grid = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
];

fn get_indices(grid: &Grid) -> HashMap<char, (C, C)> {
    let mut map = HashMap::new();
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            map.insert(grid[i][j], (i as C, j as C));
        }
    }
    map
}

fn solve(
    k: usize,
    dir_char: &char,
    dir_map: &HashMap<char, (C, C)>,
    dir_to_char: &HashMap<(C, C), char>,
    state: &mut State,
    mem: &mut HashMap<(usize, char, (C, C)), u64>,
) -> u64 {
    if k == state.len() {
        return 1
    }
    let (target_i, target_j) = *dir_map.get(dir_char).unwrap();
    if let Some(res) = mem.get(&(k, *dir_char, state[k])) {
        state[k] = (target_i, target_j);
        return *res;
    }
    let mut res = u64::MAX;
    let (i, j) = state[k];
    let steps_x = target_i - i;
    let steps_y = target_j - j;
    let di = steps_x.signum();
    let dj = steps_y.signum();
    let mut order = [(di, 0, steps_x.abs()), (0, dj, steps_y.abs())];
    for _ in 0..2 {
        let (mut i, mut j) = state[k];
        let mut temp = 0;
        let mut state = state.clone();
        let mut broke = false;
        for (di, dj, steps) in order {
            for _ in 0..steps {
                let next_dir_char = dir_to_char.get(&(di, dj)).unwrap();
                temp += solve(k+1, next_dir_char, dir_map, dir_to_char, &mut state, mem);
                i += di;
                j += dj;
                if (i, j) == (0, 0) {
                    broke = true;
                }
            }
        }
        temp += solve(k+1, &'A', dir_map, dir_to_char, &mut state, mem);
        if !broke {
            res = res.min(temp);
        }
        order.reverse();
    }
    mem.insert((k, *dir_char, state[k]), res);
    state[k] = (target_i, target_j);
    return res;
}


fn main() {
    let dir_to_char: HashMap<(C, C), char> = HashMap::from([((0, 1), '>'), ((-1, 0), '^'), ((0, -1), '<'), ((1, 0), 'v')]);

    let mut res = 0;
    let num_map = get_indices(&NUMPAD);
    let dir_map = get_indices(&DIRPAD);
    let mut mem = HashMap::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut state = [(0, 2); ROBOTS-1];
        let mut pos = (3, 2);
        let code: Vec<char> = line.chars().collect();
        let mut total = 0;
        for char in &code {
            let mut add = u64::MAX;
            let next_pos = num_map.get(char).unwrap();
            let (steps_x, steps_y) = (next_pos.0 - pos.0, next_pos.1 - pos.1);
            let dx = steps_x.signum();
            let dy = steps_y.signum();
            let mut order = [(dx, 0, steps_x.abs()), (0, dy, steps_y.abs())];

            for _ in 0..2 {
                let (mut i, mut j) = pos;
                //let mut state = state.clone();
                let mut temp = 0;
                let mut broke = false;
                for (dx, dy, steps) in order {
                    for _ in 0..steps {
                        let dir_char = dir_to_char.get(&(dx, dy)).unwrap();
                        temp += solve(0, dir_char, &dir_map, &dir_to_char, &mut state, &mut mem);
                        i += dx;
                        j += dy;
                        if (i, j) == (3, 0) {
                            broke = true;
                        }
                    }
                }
                temp += solve(0, &'A', &dir_map, &dir_to_char, &mut state, &mut mem);
                if !broke {
                    add = add.min(temp);
                }
                order.reverse();
            }
            total += add;
            pos = *next_pos;
        }
        println!("{}", total);
        let numeric_part: u64 = code.iter().filter(|x| x.is_numeric()).collect::<String>().parse().unwrap();
        res += total*numeric_part;
    }
    println!("{}", res);
}
