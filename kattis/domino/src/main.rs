use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const N: usize = 2000;

fn main() {
    let mut io = IO::new();
    let (n, p): (usize, u8) = io.r2();
    let mut grid: [[u32; N]; N] = [[0; N]; N];
    let mut visited: [[bool; N]; N] = [[false; N]; N];

    for i in 0..n {
        for (j, x) in io.line().enumerate() {
            grid[i][j] = x;
        }
    }
    
    let mut arr: Vec<(usize, usize, usize, usize)> = Vec::new();
    let mut t = 0;
    for i in 0..n {
        for j in 0..n {
            t += grid[i][j];
            for (x, y) in [(i+1, j), (i, j+1)] {
                if x < n && y < n {
                    arr.push((i, j, x, y))
                }
            }
        }
    }
    arr.sort_unstable_by_key(|x| -((grid[x.0][x.1] + grid[x.2][x.3]) as i32));
    println!("{}", t - solve(0, 0, p, &arr, &mut visited, &grid, n as isize))

}


fn solve(k: usize, c: u8, p: u8, arr: &Vec<(usize, usize, usize, usize)>, visited: &mut [[bool; N]; N], grid: &[[u32; N]; N], n: isize) -> u32 {
    if k == arr.len() || c == p {
        return 0
    }
    let (i, j, x, y) = arr[k];
    if visited[i][j] || visited[x][y] {
        return solve(k+1, c, p, arr, visited, grid, n)
    }
    let mut res = 0;
    for (a, b) in [(i as isize, j as isize), (x as isize, y as isize)] {
        for (da, db) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
            let q = a + da;
            let w = b + db;
            if q < 0 || q >= n || w < 0 || w >= n || visited[q as usize][w as usize] {
                continue
            }
            visited[a as usize][b as usize] = true;
            visited[q as usize][w as usize] = true;
            res = res.max(grid[a as usize][b as usize] + grid[q as usize][w as usize] + solve(k+1, c+1, p, arr, visited, grid, n));
            visited[a as usize][b as usize] = false;
            visited[q as usize][w as usize] = false;
        }
    }
    return res
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

    fn lineln<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecln<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.lineln(n).collect();
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
        let vec_string = vec.iter().map(|x| x.to_string() + " ").collect::<String>();
        println!("{}", vec_string);
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
