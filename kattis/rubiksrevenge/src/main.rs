use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};
use std::collections::{HashMap, VecDeque};

fn main() {
    let mut io = IO::new();
    let mut solved: [[u8; 4]; 4] = [[0; 4]; 4];
    for (i, c) in ['R', 'G', 'B', 'Y'].iter().enumerate() {
        for j in 0..4 {
            solved[i][j] = *c as u8;
        }
    }
    let mut start = [[0; 4]; 4];
    for i in 0..4 {
        for (j, char) in io.chars().enumerate() {
            start[i][j] = char as u8
        }
    }
    let mut mem1 = HashMap::new();
    let mut mem2 = HashMap::new();
    mem1.insert(start, 0);
    mem2.insert(solved, 0);
    let mut q = VecDeque::new();
    q.push_back((start, 0, 0));
    q.push_back((solved, 0, 1));
    while let Some((grid, s, t)) = q.pop_front() {
        let (mem, other_mem) = {
            if t == 0 {
                (&mut mem1, &mut mem2)
            } else {
                (&mut mem2, &mut mem1)
            }
        };

        match other_mem.get(&grid) {
            Some(v) => {println!("{}", s+v); return},
            None => {}
        };
        for i in 0..4 {
            for (dx, dy) in [(0, 1), (0, -1)] {
                let new_grid = move_grid(i, 0, dx, dy, &grid);
                match mem.entry(new_grid) {
                    std::collections::hash_map::Entry::Occupied(_) => continue,
                    std::collections::hash_map::Entry::Vacant(vacant_entry) => {
                        vacant_entry.insert(s+1);
                        q.push_back((new_grid, s+1, t));
                    }
                };
            }

            for (dx, dy) in [(1, 0), (-1, 0)] {
                let new_grid = move_grid(0, i, dx, dy, &grid);
                match mem.entry(new_grid) {
                    std::collections::hash_map::Entry::Occupied(_) => continue,
                    std::collections::hash_map::Entry::Vacant(vacant_entry) => {
                        vacant_entry.insert(s+1);
                        q.push_back((new_grid, s+1, t));
                    }
                };
            }
        }
    }
}


fn move_grid(mut i: usize, mut j: usize, dx: isize, dy: isize, grid: &[[u8; 4]; 4]) -> [[u8; 4]; 4] {
    let mut grid = grid.clone();
    let mut cur = grid[i][j];
    for _ in 0..4 {
        let x = ((i as isize+dx).rem_euclid(4)) as usize;
        let y = ((j as isize+dy).rem_euclid(4)) as usize;
        (cur, grid[x][y]) = (grid[x][y], cur);
        (i, j) = (x, y);
    }
    return grid
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
        unsafe { s.parse::<T>().unwrap_unchecked() }
    }

    fn parse_next<T: FromStr>(&self, line_split: &mut SplitAsciiWhitespace) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
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

    fn line<T: FromStr>(&mut self) -> impl Iterator<Item = T> + '_ {
        self._rl();
        return self.buf.split_ascii_whitespace().map(|x| self.parse(x));
    }

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
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

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}