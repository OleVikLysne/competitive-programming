use std::collections::HashSet;

#[allow(non_snake_case)]
fn main() {
    let B = 10_i64.pow(9)+9;
    let A = 97; // cool prime number


    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: u32 = buf.trim().parse().unwrap();
    buf.clear();

    let mut hashes = HashSet::new();
    let mut lengths = HashSet::new();
    let mut words = Vec::new();
    let mut words_set = HashSet::new();
    for _ in 0..n {
        let _ = stdin.read_line(&mut buf);
        let word: Vec<u8> = buf.trim().chars().map(|x| x as u8).collect();
        let h = rolling_hash(&word, A, B);
        lengths.insert(word.len());
        hashes.insert(h);
        let temp = word.clone();
        words.push(word);
        words_set.insert(temp);
        buf.clear();
    }
    let mut found = false;
    for string in words {
        let string_hash = rolling_hash(&string, A, B);
        if !lengths.contains(&(string.len()-1)) {
            continue;
        }

        let k = string.len()-1;
        let mut typo_hash = ( string_hash - string[0] as i64 * pow_mod(A, k, B) ).rem_euclid(B);
        if hashes.contains(&typo_hash) {
            let mut temp: Vec<u8> = Vec::with_capacity(string.len()-1);
            temp.extend(string[1..].iter());
            if words_set.contains(&temp) {
                found = true;
                println!("{}", String::from_utf8(string).unwrap());
                continue
            }
        }
        for i in 1..string.len() {
            typo_hash -= (string[i] as i64 * pow_mod(A, k-i, B)).rem_euclid(B);
            typo_hash += (string[i-1] as i64 * pow_mod(A, k-i, B)).rem_euclid(B);
            typo_hash = typo_hash.rem_euclid(B);
            if hashes.contains(&typo_hash) {
                let mut temp: Vec<u8> = Vec::with_capacity(string.len()-1);
                temp.extend(string[..i].iter());
                temp.extend(string[i+1..].iter());
                if words_set.contains(&temp) {
                    found = true;
                    println!("{}", String::from_utf8(string).unwrap());
                    break
                }
            }
        }

    }
    if !found {
        println!("NO TYPOS")
    }
}

#[allow(non_snake_case)]
fn rolling_hash(string: &[u8], A: i64, B: i64) -> i64 {
    let k = string.len()-1;
    let mut hashed_str = 0;
    for (i, s) in string.iter().enumerate() {
        hashed_str += (*s as i64 * pow_mod(A, k-i, B)) % B;
        hashed_str %= B;
    }
    hashed_str
}

#[allow(non_snake_case)]
fn pow_mod(mut A: i64, mut exp: usize, B: i64) -> i64 {
    if B == 1 { return 0 }
    let mut res = 1;
    while exp > 0 {
        if exp % 2 == 1 {
            res = (res * A) % B;
        }
        exp = exp >> 1;
        A = (A * A) % B
    }
    res
}