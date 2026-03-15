use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const MAX: usize = 1 << 19;

fn main() {
    let mut io = IO::new();
    let n: usize = io.r();
    let mut counts = [0; 100];
    for x in io.line::<usize>() {
        counts[x] += 1;
    }
    let mut transform = [Complex { real: 1.0 / MAX as f64, imag: 0.0 }; MAX];
    let angle = 2.0 * std::f64::consts::PI / MAX as f64;
    let w = Complex {
        real: f64::cos(angle),
        imag: f64::sin(angle),
    };

    for i in 1..100 {
        if counts[i] == 0 {continue}
        let c = &counts[i];
        let p = Complex { real: (i as f64) / 100.0, imag: 0.0 };
        let q = Complex { real: 1.0 - (i as f64) / 100.0, imag: 0.0 };
        let mut wj = Complex { real: 1.0, imag: 0.0 };
        for j in 0..MAX/2 {
            transform[j] *= (q + wj*p).pow(*c);
            transform[j+MAX/2] *= (q - wj*p).pow(*c);
            wj *= w;
        }
    }
    let inv = fft(&transform, true);
    for i in 0..n+1 {
        print!("{} ", inv[i].real);
    }
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

    fn pow(&self, n: i32) -> Self {
        let (r, theta) = self.polar();
        let l = r.powi(n);
        let real = l * (n as f64*theta).cos();
        let imag = l * (n as f64*theta).sin();
        return Complex{real, imag}
    }

    fn polar(&self) -> (f64, f64) {
        let r = (self.real.powi(2)+self.imag.powi(2)).sqrt();
        let mut denom = self.real;
        if denom == 0.0 {
            denom = 0.00001;
        }
        let mut theta = (self.imag/denom).atan();
        if self.real < 0.0 {
            theta += std::f64::consts::PI;
        }
        return (r, theta)

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


fn fft(coef: &[Complex], inverse: bool) -> Vec<Complex> {
    let n = coef.len();
    if n == 1 {
        return coef.to_vec()
    }
    let a_coef: Vec<Complex> = coef.iter().step_by(2).map(|x| *x).collect();
    let b_coef: Vec<Complex> = coef[1..].iter().step_by(2).map(|x| *x).collect();
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