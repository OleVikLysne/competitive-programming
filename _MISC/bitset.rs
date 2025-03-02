#[derive(Clone, Debug)]
struct Bitset {
    v: Vec<u128>,
}

#[allow(dead_code)]
impl Bitset {
    const BITS: usize = 128;

    fn new(n: usize) -> Self {
        Bitset {
            v: vec![0; (n - 1) / Self::BITS + 1],
        }
    }

    fn _get_idxs(&self, i: &usize) -> (usize, usize) {
        let j = i / Self::BITS;
        let k = i % Self::BITS;
        return (j, k)
    }

    fn set(&mut self, i: usize) {
        let (j, k) = self._get_idxs(&i);
        self.v[j] |= 1 << k
    }

    fn flip(&mut self, i: usize) {
        let (j, k) = self._get_idxs(&i);
        self.v[j] ^= 1 << k;
    }
}


impl std::ops::Index<usize> for Bitset {
    type Output = bool;

    fn index(&self, i: usize) -> &Self::Output {
        let (j, k) = self._get_idxs(&i);
        if self.v[j] & 1 << k != 0 {
            return &true;
        }
        return &false;
    }
}

impl std::ops::BitAnd<&Bitset> for &Bitset {
    type Output = Bitset;

    fn bitand(self, rhs: &Bitset) -> Self::Output {
        let mut res = self.clone();
        for i in 0..rhs.v.len() {
            res.v[i] &= rhs.v[i];
        }
        return res;
    }
}

impl std::ops::BitXor<&Bitset> for &Bitset {
    type Output = Bitset;

    fn bitxor(self, rhs: &Bitset) -> Self::Output {
        let mut res = self.clone();
        for i in 0..rhs.v.len() {
            res.v[i] ^= rhs.v[i];
        }
        return res;
    }
}

impl std::ops::BitOr<&Bitset> for &Bitset {
    type Output = Bitset;

    fn bitor(self, rhs: &Bitset) -> Self::Output {
        let mut res = self.clone();
        for i in 0..rhs.v.len() {
            res.v[i] |= rhs.v[i];
        }
        return res;
    }
}

impl std::ops::BitOrAssign<&Bitset> for Bitset {
    fn bitor_assign(&mut self, rhs: &Bitset) {
        for i in 0..self.v.len() {
            self.v[i] |= rhs.v[i];
        }
    }
}
impl std::ops::BitXorAssign<&Bitset> for Bitset {
    fn bitxor_assign(&mut self, rhs: &Bitset) {
        for i in 0..self.v.len() {
            self.v[i] ^= rhs.v[i];
        }
    }
}
impl std::ops::BitAndAssign<&Bitset> for Bitset {
    fn bitand_assign(&mut self, rhs: &Bitset) {
        for i in 0..self.v.len() {
            self.v[i] &= rhs.v[i];
        }
    }
}