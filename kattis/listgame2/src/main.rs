use std::collections::{HashMap, HashSet};
const MAX_VAL: usize = 31622777;


fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: u64 = buf.trim().parse().unwrap();
    let primes = sieve();
    let mut s1: i16 = 0;
    let mut keys = Vec::new();
    let mut factors1: HashMap<u64, u16> = factorize(n, &primes);
    let mut seen1 = HashSet::new();
    seen1.insert(1);
    for (key, val) in factors1.iter_mut() {
        *val -= 1;
        s1 += 1;
        seen1.insert(*key);
        if *val > 0 {
            keys.push(*key);
        }
    }

    let mut s2 = s1;
    let mut seen2 = seen1.clone();
    let mut factors2 = factors1.clone();
    s2 += initial_reduction(&mut factors2, &mut seen2, &mut keys);

    for size in 2..=50 { // ceil(log2(10^15))
        while search(&mut Vec::new(), &mut factors1, &mut seen1, 1, &mut keys, size) {
            s1 += 1;
        }
        while search(&mut Vec::new(), &mut factors2, &mut seen2, 1, &mut keys, size) {
            s2 += 1
        }
    }

    println!("{}", s1.max(s2));
}


fn search(
    collected: &mut Vec<u64>,
    factors: &mut HashMap<u64, u16>,
    seen: &mut HashSet<u64>,
    val: u64,
    keys: &mut Vec<u64>,
    size: usize
) -> bool {

    if keys.len() == 0 {
        return false
    }

    if seen.insert(val) {
        return true
    } else if collected.len() == size {
        return false
    }

    if collected.len() == 0 {
        keys.sort_by_key(|x| -(*factors.get(x).unwrap() as i16));
    }
    if collected.len() + 1 < size && *factors.get(&keys[0]).unwrap() > 0 {
        let key = keys[0];
        collected.push(key);
        *factors.get_mut(&key).unwrap() -= 1;
        if search(collected, factors, seen, key*val, keys, size) {
            return true
        }
        *factors.get_mut(&key).unwrap() += 1;
        collected.pop();
        return false
    }

    for i in 0..keys.len() {
        let key = keys[i];
        if *factors.get(&key).unwrap() == 0 { continue }
        let new_val = key * val;
        collected.push(key);
        *factors.get_mut(&key).unwrap() -= 1;
        if search(collected, factors, seen, new_val, keys, size) {
            return true
        }
        collected.pop();
        *factors.get_mut(&key).unwrap() += 1;
    }
    return false
}


fn initial_reduction(
    factors: &mut HashMap<u64, u16>,
    seen: &mut HashSet<u64>,
    keys: &mut Vec<u64>
) -> i16 {
    if keys.len() == 0 {
        return 0;
    }
    let mut s = 0;
    keys.sort_by_key(|x| -(*factors.get(x).unwrap() as i16));
    let mut success = true;
    while success {
        success = false;
        for i in 0..keys.len()-1 {
            let mut size = 2;
            loop {
                while seen.contains(&(keys[i].pow(size as u32))) {
                    size += 1;
                }
                if *factors.get(&keys[i]).unwrap() <= *factors.get(&keys[i+1]).unwrap() + size {
                    break
                }
                *factors.get_mut(&keys[i]).unwrap() -= size;
                seen.insert(keys[i].pow(size as u32));
                s += 1;
                success = true;
                
            }
        } 
    }
    return s;
}




fn sieve() -> Vec<u64> {
    let mut prime: [bool; MAX_VAL] = [true; MAX_VAL];
    let mut l = Vec::new();
    prime[0] = false;
    prime[1] = false;
    for i in 2..MAX_VAL {
        if !prime[i] {
            continue
        }
        l.push(i as u64);
        for j in (i*2..MAX_VAL).step_by(i) {
            prime[j] = false;
        }
    }
    return l
}


fn factorize(mut n: u64, primes: &[u64]) -> HashMap<u64, u16> {
    let mut factors: HashMap<u64, u16> = HashMap::new();
    for p in primes {
        if p*p > n { break }
        if n % p == 0 {
            while n % p == 0 {
                *factors.entry(*p).or_insert(0) += 1;
                n /= p;
            }
        }
    }
    if n > 1 {
        *factors.entry(n).or_insert(0) += 1;
    }
    return factors
}