use std::collections::HashSet;
use std::fmt::Display;
use std::io::Read;
use std::process::exit;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

fn add(x: f32, y: f32) -> f32 {
    x + y
}
fn sub(x: f32, y: f32) -> f32 {
    x - y
}
fn mul(x: f32, y: f32) -> f32 {
    x * y
}
fn div(x: f32, y: f32) -> f32 {
    x / y
}

const OPS: [fn(f32, f32) -> f32; 4] = [add, sub, mul, div];
const OP_STR: [char; 4] = ['+', '-', '*', '/'];

fn main() {
    let mut io = IO::new();
    let (c, t): (usize, f32) = io.r2();
    let mut nums: Vec<(f32, u8)> = Vec::new();
    for x in io.line() {
        nums.push((x, 1));
    }
    let mut numbers: Vec<(f32, u8)> = Vec::new();
    let mut visited = vec![false; c];
    let mut nums_visited = vec![false; c];
    let mut parent: Vec<(usize, usize, usize)> = vec![(0, 0, 0); c];
    solve(&nums, &mut numbers, &mut visited, &mut nums_visited, &mut parent, c, t);
}


fn reconstruct(
    nums:  &[(f32, u8)],
    parent: &Vec<(usize, usize, usize)>,
    k: usize,
    c: usize
) -> Vec<char> {
    let mut res = Vec::new();
    if k < c {
        return (nums[k].0.round() as u8).to_string().chars().collect()
    }
    res.push('(');
    let (i, j, op_idx) = parent[k];
    res.extend(reconstruct(nums, parent, i, c).iter());
    res.push(OP_STR[op_idx]);
    res.extend(reconstruct(nums, parent, j, c).iter());
    res.push(')');
    return res
    

}

fn foo(
    nums: &[(f32, u8)],
    numbers: &mut Vec<(f32, u8)>,
    visited: &mut Vec<bool>,
    parent: &mut Vec<(usize, usize, usize)>,
    c: usize,
    t: f32,
    seen: &mut HashSet<String>
) {

    let mut state = Vec::new();
    for i in 0..numbers.len() {
        if !visited[i] {
            state.push(numbers[i].0);
        }
    }
    state.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let state = format!("{:?}", state);
    if !seen.insert(state) {
        return
    }
    for i in 0..numbers.len() {
        if visited[i] { continue }
        for j in 0..numbers.len() {
            if visited[j] || i == j { continue }
            visited[i] = true;
            visited[j] = true;
            let (x, xc) = numbers[i];
            let (y, yc) = numbers[j];
            for op_idx in 0..4 {
                let op = OPS[op_idx];
                if op_idx == 3 && y == 0.0 { continue }
                let z = op(x, y);
                let zc = xc+yc;
                parent.push((i, j, op_idx));
                if zc == c as u8 && (z+1e-4 < t) != (z-1e-4 < t) {
                    for char in reconstruct(nums, parent, numbers.len(), c) {
                        print!("{}", char);
                    }
                    exit(0);
                }
                visited.push(false);
                numbers.push((z, zc));
                foo(nums, numbers, visited, parent, c, t, seen);
                visited.pop();
                numbers.pop();
                parent.pop();
            }
            visited[i] = false;
            visited[j] = false;


        }
    }
}

fn solve(
    nums: &[(f32, u8)],
    numbers: &mut Vec<(f32, u8)>,
    visited: &mut Vec<bool>,
    nums_visited: &mut Vec<bool>,
    parent: &mut Vec<(usize, usize, usize)>,
    c: usize,
    t: f32
) {
    if numbers.len() == c {
        foo(nums, numbers, visited, parent, c, t, &mut HashSet::new());
    }
    for i in 0..c {
        if nums_visited[i] {continue}
        numbers.push(nums[i]);
        nums_visited[i] = true;

        solve(nums, numbers, visited, nums_visited, parent, c, t);

        nums_visited[i] = false;
        numbers.pop();
        
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
