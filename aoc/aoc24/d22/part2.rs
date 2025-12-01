use std::collections::{HashMap, HashSet, VecDeque};

const MOD: i64 = 16777216;
const STEPS: u32 = 2000;

fn evolve(mut bit_string: i64) -> Vec<i64> {
    let mut res = vec![bit_string];
    for _ in 0..STEPS {
        bit_string ^= bit_string * 64;
        bit_string %= MOD;
        
        bit_string ^= bit_string / 32;
        bit_string %= MOD;
        
        bit_string ^= bit_string * 2048;
        bit_string %= MOD;
        res.push(bit_string);
    }
    res
}

fn main() {
    let mut map = HashMap::new();
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut seen = HashSet::new();
        let bit_string: i64 = line.parse().unwrap();
        let sequence = evolve(bit_string);
        let mut prev = sequence[0] % 10;
        let mut pattern = VecDeque::new();
        for elem in &sequence[1..4] {
            let price = elem % 10;
            pattern.push_back(price-prev);
            prev = price;
        }
        for elem in &sequence[4..] {
            let price = elem % 10;
            pattern.push_back(price-prev);
            prev = price;
            if seen.insert(pattern.clone()) {
                *map.entry(pattern.clone()).or_insert(0) += price;
            }
            pattern.pop_front();
        }
    }
    println!("{}", map.values().max().unwrap());
}