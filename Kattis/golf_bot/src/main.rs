use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

fn main() {
    let mut io = IO::new();
    let n: usize = io.r();
    let mut poly = vec![Complex::new(); 1 << 19];
    for x in io.linenl::<usize>(n) {
        poly[x] += 1.0;
    }
    poly[0] += 1.0;
    let res = multiply(&poly, &poly);
    let mut total = 0;
    let m: usize = io.r();
    for x in io.linenl::<usize>(m) {
        if res[x] > 0 {
            total += 1;
        }
    }
    println!("{}", total)
}

#[derive(Debug, Copy, Clone)]
struct Complex {
    real: f64,
    imag: f64,
}

impl Complex {
    fn new() -> Self {
        Complex {
            real: 0.0,
            imag: 0.0,
        }
    }
}

impl std::ops::Mul<Complex> for Complex {
    type Output = Complex;

    fn mul(self, other: Complex) -> Complex {
        return Complex {
            real: self.real * other.real - self.imag * other.imag,
            imag: self.real * other.imag + self.imag * other.real,
        };
    }
}
impl std::ops::MulAssign<Complex> for Complex {
    fn mul_assign(&mut self, other: Complex) {
        let new_r = self.real * other.real - self.imag * other.imag;
        self.imag = self.real * other.imag + self.imag * other.real;
        self.real = new_r;
    }
}

impl std::ops::Add<Complex> for Complex {
    type Output = Complex;

    fn add(self, other: Complex) -> Complex {
        return Complex {
            real: self.real + other.real,
            imag: self.imag + other.imag,
        };
    }
}

impl std::ops::Add<f64> for Complex {
    type Output = Complex;

    fn add(self, other: f64) -> Complex {
        return Complex {
            real: self.real + other,
            imag: self.imag
        };
    }
}

impl std::ops::AddAssign<f64> for Complex {

    fn add_assign(&mut self, other: f64)  {
        self.real += other
    }
}

impl std::ops::Sub<Complex> for Complex {
    type Output = Complex;

    fn sub(self, other: Complex) -> Complex {
        return Complex {
            real: self.real - other.real,
            imag: self.imag - other.imag,
        };
    }
}

impl std::ops::Div<f64> for Complex {
    type Output = Complex;

    fn div(self, other: f64) -> Complex {
        return Complex {
            real: self.real / other,
            imag: self.imag,
        };
    }
}

fn fft(coef: &Vec<Complex>, inverse: bool) -> Vec<Complex> {
    let n = coef.len();
    if n == 1 {
        return coef.clone();
    }

    let mut a_coef = vec![Complex::new(); n / 2];
    let mut b_coef = vec![Complex::new(); n / 2];
    for i in 0..n / 2 {
        a_coef[i] = coef[2 * i];
        b_coef[i] = coef[2 * i + 1];
    }
    let a_fft = fft(&a_coef, inverse);
    let b_fft = fft(&b_coef, inverse);

    let mut angle = 2.0 * std::f64::consts::PI / (n as f64);
    if inverse {
        angle = -angle;
    }
    let w = Complex {
        real: f64::cos(angle),
        imag: f64::sin(angle),
    };
    let mut wj = Complex {
        real: 1.0,
        imag: 0.0,
    };
    let mut res = vec![Complex::new(); n];
    for j in 0..n / 2 {
        res[j] = a_fft[j] + wj * b_fft[j];
        res[j + n / 2] = a_fft[j] - wj * b_fft[j];
        wj *= w;
    }
    return res;
}

fn multiply(p1: &Vec<Complex>, p2: &Vec<Complex>) -> Vec<i64> {
    let n = p1.len();
    let mut transform = fft(p1, false);
    for (i, x) in fft(p2, false).iter().enumerate() {
        transform[i] *= *x;
    }
    let rev_transform = fft(&transform, true);
    return rev_transform
        .iter()
        .map(|x| ((x.real / n as f64).round()) as i64)
        .collect();
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
