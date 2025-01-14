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

fn fft(coef: &[Complex], inverse: bool) -> Vec<Complex> {
    let n = coef.len();
    if n == 1 {
        return coef.to_vec()
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

fn multiply(p1: &[Complex], p2: &[Complex]) -> Vec<i64> {
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