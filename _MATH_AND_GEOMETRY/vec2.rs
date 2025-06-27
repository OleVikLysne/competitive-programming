// Several methods have not been stress tested
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

    fn normalize_inplace(&mut self) {
        if self.is_zero_vec() {
            return;
        }
        *self /= self.length();
    }

    fn normalize(&self) -> Self {
        if self.is_zero_vec() {
            return self.clone();
        }
        return *self / self.length();
    }

    fn cross(&self, other: &Vec2) -> f64 {
        return self.x * other.y - self.y * other.x;
    }

    fn dot(&self, other: &Vec2) -> f64 {
        return self.x * other.x + self.y * other.y;
    }

    fn orient(&self, v1: &Vec2, v2: &Vec2) -> f64 {
        let v3 = *v1 - *self;
        let v4 = *v2 - *self;
        return v3.cross(&v4);
    }

    fn squared_dist(&self, other: &Vec2) -> f64 {
        return (self.x - other.x).powi(2) + (self.y - other.y).powi(2);
    }

    fn dist(&self, other: &Vec2) -> f64 {
        return self.squared_dist(other).sqrt();
    }

    fn rotate_rad(&self, theta: f64) -> Self {
        let cos_theta = theta.cos();
        let sin_theta = theta.sin();
        return Vec2 {
            x: self.x * cos_theta - self.y * sin_theta,
            y: self.x * sin_theta + self.y * cos_theta,
        };
    }

    fn rotate(&self, theta: f64) -> Self {
        return self.rotate_rad(theta.to_radians());
    }

    fn angle_rad(&self, other: &Vec2) -> f64 {
        return self.normalize().dot(&other.normalize()).acos();
    }

    fn angle(&self, other: &Vec2) -> f64 {
        return self.angle_rad(other).to_degrees();
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

impl std::ops::Div<f64> for Vec2 {
    type Output = Vec2;

    fn div(self, rhs: f64) -> Self::Output {
        return Vec2 {
            x: self.x / rhs,
            y: self.y / rhs,
        };
    }
}

impl std::ops::Mul<f64> for Vec2 {
    type Output = Vec2;

    fn mul(self, rhs: f64) -> Self::Output {
        return Vec2 {
            x: self.x * rhs,
            y: self.y * rhs,
        };
    }
}

impl std::ops::AddAssign<Vec2> for Vec2 {
    fn add_assign(&mut self, other: Vec2) {
        self.x += other.x;
        self.y += other.y;
    }
}

impl std::ops::SubAssign<Vec2> for Vec2 {
    fn sub_assign(&mut self, other: Vec2) {
        self.x -= other.x;
        self.y -= other.y;
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

impl std::ops::Neg for Vec2 {
    type Output = Vec2;

    fn neg(self) -> Self::Output {
        return Vec2 {
            x: -self.x,
            y: -self.y,
        };
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