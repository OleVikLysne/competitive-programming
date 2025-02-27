use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

#[derive(Debug, Copy, Clone)]
struct Vec2 {
    x: f64,
    y: f64,
}

#[allow(dead_code)]
impl Vec2 {
    fn new() -> Self {
        return Vec2 { x: 0.0, y: 0.0 };
    }

    fn is_zero_vec(&self) -> bool {
        return self.x == 0.0 && self.y == 0.0;
    }

    fn length(&self) -> f64 {
        return (self.x.powi(2) + self.y.powi(2)).sqrt();
    }

    fn normalize(&mut self) {
        if self.is_zero_vec() {
            return;
        }
        *self /= self.length();
    }

    fn cross(&self, other: &Vec2) -> f64 {
        return self.x * other.y - self.y * other.x;
    }

    fn orient(&self, v1: &Vec2, v2: &Vec2) -> f64 {
        let v3 = *v1 - *self;
        let v4 = *v2 - *self;
        return v3.cross(&v4);
    }

    fn squared_dist(&self, other: &Vec2) -> f64 {
        return (self.x - other.x).powi(2) + (self.y - other.y).powi(2);
    }
}

impl std::ops::Add<Vec2> for Vec2 {
    type Output = Vec2;

    fn add(self, rhs: Vec2) -> Self::Output {
        return Vec2 {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        };
    }
}

impl std::ops::Sub<Vec2> for Vec2 {
    type Output = Vec2;

    fn sub(self, rhs: Vec2) -> Self::Output {
        return Vec2 {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        };
    }
}

impl std::ops::MulAssign<f64> for Vec2 {
    fn mul_assign(&mut self, other: f64) {
        self.x *= other;
        self.y *= other;
    }
}

impl std::ops::DivAssign<f64> for Vec2 {
    fn div_assign(&mut self, other: f64) {
        self.x /= other;
        self.y /= other;
    }
}

fn intersect(line1: (&Vec2, &Vec2), line2: (&Vec2, &Vec2)) -> Option<Vec2> {
    let (a, b) = line1;
    let (c, d) = line2;
    let oa = c.orient(d, a);
    let ob = c.orient(d, b);
    let oc = a.orient(b, c);
    let od = a.orient(b, d);
    if oa * ob < 0.0 && oc * od < 0.0 {
        let x = (a.x * ob - b.x * oa) / (ob - oa);
        let y = (a.y * ob - b.y * oa) / (ob - oa);
        return Some(Vec2 { x, y });
    }
    return None;
}

fn line_poly_intersect(line: (&Vec2, &Vec2), poly: &[Vec2]) -> bool {
    for i in 0..poly.len() {
        let line2 = (&poly[i], &poly[(i + 1) % poly.len()]);
        if intersect(line, line2).is_some() {
            return true;
        }
    }
    return false;
}

fn sign(x: f64) -> f64 {
    if x < 0.0 {
        return -1.0;
    }
    if x == 0.0 {
        return 0.0;
    }
    return 1.0;
}

const DELTA: f64 = 1e-6;

fn main() {
    let mut io = IO::new();
    let (n, l): (usize, f64) = io.r2();
    let mut polys = Vec::with_capacity(n);
    let mut polys_ext = Vec::with_capacity(n);
    for _ in 0..n {
        let (mut x1, mut y1, mut x2, mut y2) = io.r4();
        polys.push(vec![
            Vec2 { x: x1, y: y1 },
            Vec2 { x: x1, y: y2 },
            Vec2 { x: x2, y: y2 },
            Vec2 { x: x2, y: y1 },
        ]);
        x1 -= DELTA;
        y1 -= DELTA;
        x2 += DELTA;
        y2 += DELTA;
        polys_ext.push(vec![
            Vec2 { x: x1, y: y1 },
            Vec2 { x: x1, y: y2 },
            Vec2 { x: x2, y: y2 },
            Vec2 { x: x2, y: y1 },
        ]);
    }

    let mut best = 1;
    for i in 0..n {
        for v in &polys[i] {
            for j in 0..n {
                if best == n {
                    println!("{}", best);
                    return;
                }
                if i == j {
                    continue;
                }
                let poly = &polys[j];
                let idx = (0..4)
                    .min_by(|x, y| {
                        v.squared_dist(&poly[*x])
                            .partial_cmp(&v.squared_dist(&poly[*y]))
                            .unwrap()
                    })
                    .unwrap();
                for v2 in [&polys[j][(idx + 1) % 4], &polys[j][(idx + 3) % 4]] {
                    let mut x1 = poly[idx].x;
                    let mut y1 = poly[idx].y;
                    let x2 = v2.x;
                    let y2 = v2.y;
                    let dx = sign(x2 - x1);
                    let dy = sign(y2 - y1);
                    loop {
                        let start = Vec2 { x: x1, y: y1 };
                        if v.squared_dist(&start) <= l.powi(2) {
                            let mut dir = *v - start;
                            dir.normalize();
                            dir *= l;
                            let line = (&start, &(start + dir));
                            let mut c = 2;
                            for k in 0..n {
                                if k == i || k == j {
                                    continue;
                                }
                                if line_poly_intersect(line, &polys_ext[k]) {
                                    c += 1
                                }
                            }
                            best = best.max(c);
                        }
                        if x1 == x2 && y1 == y2 {
                            break;
                        }
                        x1 += dx;
                        y1 += dy;
                    }
                }
            }
        }
    }
    println!("{}", best);
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
