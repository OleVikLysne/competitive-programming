use std::collections::{HashMap, VecDeque};
use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const DIRS: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

const DIR_WORD: [&str; 4] = ["east", "south", "west", "north"];

fn get_path(mut state: usize, pred: &HashMap<usize, usize>) -> Vec<usize> {
    let mut path = vec![];
    while let Some(&prev) = pred.get(&state) {
        if state == prev {break}
        state = prev;
        let l = (state & 3) as usize;
        state ^= l;
        path.push(l);
    }
    path.reverse();
    path
}

fn main() {
    let mut io = IO::new();
    let n: usize = io.r();
    let mut grid = [[false; 8]; 8];
    for i in 0..n {
        for (j, c) in io.chars().enumerate() {
            if c == 'O' {
                grid[i][j] = true;
            }
        }
    }
    let grid = grid;
    let mut state: usize = 0;
    for i in 1..n - 1 {
        for j in 1..n - 1 {
            if !grid[i][j] {
                state |= 1 << (i * 8 + j);
            }
        }
    }
    let mut pred = HashMap::new();
    pred.insert(state, state);
    let mut q = VecDeque::from([state]);
    while let Some(state) = q.pop_front() {
        for l in 0..DIRS.len() {
            let (di, dj) = DIRS[l];
            let mut new_state = 0;
            for k in 0..64 {
                if state & (1 << k) == 0 {
                    continue;
                }
                let i = k / 8;
                let j = k % 8;
                let x = (i as isize + di) as usize;
                let y = (j as isize + dj) as usize;
                if grid[x][y] {
                    new_state |= 1 << (i * 8 + j);
                } else if 0 < x && x < n - 1 && 0 < y && y < n - 1 {
                    new_state |= 1 << (x * 8 + y);
                }
            }
            if !pred.contains_key(&new_state) {
                pred.insert(new_state, state + l);
                if new_state == 0 {
                    let path = get_path(new_state, &pred);
                    for x in path {
                        print!("{} ", DIR_WORD[x]);
                    }
                    return;
                }
                q.push_back(new_state);
            }
        }
    }
}

struct IO {
    buf: String,
    stdin: std::io::Stdin,
}

#[allow(dead_code)]
impl IO {
    fn new() -> Self {
        IO {
            buf: String::new(),
            stdin: std::io::stdin(),
        }
    }

    fn _rl(&mut self) {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
    }

    fn parse<T: FromStr>(&self, s: &str) -> T {
        unsafe { s.parse().unwrap_unchecked() }
    }

    fn parse_next<T: FromStr>(&self, line_split: &mut SplitAsciiWhitespace) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
    }

    fn line<T: FromStr>(&mut self) -> impl Iterator<Item = T> + '_ {
        self._rl();
        return self.buf.split_ascii_whitespace().map(|x| self.parse(x));
    }

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
    }

    fn chars(&mut self) -> Chars {
        self._rl();
        return self.buf.trim().chars();
    }

    fn all(&mut self) -> String {
        self.buf.clear();
        let _ = self.stdin.read_to_string(&mut self.buf);
        return self.buf.trim().to_string();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }

    fn r<T: FromStr>(&mut self) -> T {
        self._rl();
        self.parse(self.buf.trim())
    }

    fn r2<T1, T2>(&mut self) -> (T1, T2)
    where
        T1: FromStr,
        T2: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r4<T1, T2, T3, T4>(&mut self) -> (T1, T2, T3, T4)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r5<T1, T2, T3, T4, T5>(&mut self) -> (T1, T2, T3, T4, T5)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
        T5: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }
}
