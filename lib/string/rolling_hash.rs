const A: i64 = 31;
const B: i64 = 1 << 61 - 1//10_i64.pow(18)+7;

fn roll_hash(string: &[i64], k: usize) -> Vec<i64> {
    let n = string.len();
    let mut hashed_str = 0;
    let mut l = Vec::new();
    for i in 0..k as usize {
        hashed_str += string[i] * pow_mod(A, k-i-1, B);
        hashed_str = hashed_str.rem_euclid(B);
    }
    l.push(hashed_str);
    for i in k..n {
        hashed_str -= string[i-k] * pow_mod(A, k - 1, B);
        hashed_str *= A;
        hashed_str += string[i];
        hashed_str = hashed_str.rem_euclid(B);
        l.push(hashed_str);
    }
    return l
}

fn pow_mod(mut a: i64, mut exp: usize, b: i64) -> i64 {
    let mut res = 1;
    while exp > 0 {
        if exp % 2 == 1 {
            res *= a;
            res %= b;
        }
        exp >>= 1;
        a *= a;
        a %= b;
    }
    res
}