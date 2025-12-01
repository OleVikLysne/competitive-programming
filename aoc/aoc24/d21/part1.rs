use std::collections::{HashSet, VecDeque};

type C = i32;
type Grid = [[char; 3]; 4];
type State = [(C, C); 3];

const DELTAS: [(C, C); 4] = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
];

fn valid(i: &C, j: &C, grid: &Grid) -> bool {
    return 0 <= *i && *i < grid.len() as C && 0 <= *j && *j < grid[0].len() as C;
}


const NUMPAD: Grid  = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
    ];
    
const DIRPAD: Grid  = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
];

fn state_transition(dir: char) -> usize {
    return match dir {
        '>' => 0,
        '^' => 1,
        '<' => 2,
        'v' => 3,
        'A' => 4,
        _ => usize::MAX
    }
}



fn step(mut k: usize, state: &mut State, action: usize) -> Option<State> {
    if k == 0 {
        return Some(*state)
    }
    k -= 1;
    let grid = {
        if k == 0 {&NUMPAD} 
        else      {&DIRPAD}
    };
    
    let (i, j) = state[k];
    //println!("{} {}", grid[i as usize][j as usize], k);
    let next_action = state_transition(grid[i as usize][j as usize]);
    if action == 4 {
        return step(k, state, next_action)
    }
    let (di, dj) = DELTAS[action];
    let (x, y) = (i+di, j+dj);
    if !valid(&x, &y, grid) || grid[x as usize][y as usize] == ' ' {
        return None
    }
    state[k] = (x, y);
    return Some(*state)
}


// state  A A A
// target A A 0

fn main() {
    let mut res = 0;
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut starting_state = [(3, 2), (0, 2), (0, 2)];
        let code: Vec<char> = line.chars().collect();
        let mut total = 0;
        for char in &code {
            let mut visited = HashSet::from([starting_state]);
            let mut q = VecDeque::from([(starting_state, 0)]);
            while let Some((state, steps)) = q.pop_front() {
                if state[1..] == [(0, 2), (0, 2)] {
                    let (i, j) = state[0];
                    if NUMPAD[i as usize][j as usize] == *char {
                        total += steps+1;
                        starting_state = state;
                        break
                    }
                }

                for action in 0..DELTAS.len()+1 {
                    if let Some(next_state) = step(state.len(), &mut state.clone(), action) {
                        if visited.insert(next_state) {
                            q.push_back((next_state, steps+1));
                        }
                    }
                }
            }
        }
        println!("{}", total);
        let numeric_part: u32 = code.iter().filter(|x| x.is_numeric()).collect::<String>().parse().unwrap();
        res += total*numeric_part;
    }
    println!("{}", res);

}