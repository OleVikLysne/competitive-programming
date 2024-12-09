use std::collections::HashMap;

fn main() {
    let mut buf = String::new();
    let _ = std::io::stdin().read_line(&mut buf);
    let mut map: Vec<i32> = buf.trim().chars().map(|x| (x as u32 - (b'0' as u32)) as i32).collect();
    if map.len() % 2 == 0 {
        map.pop();
    }
    let mut seq = Vec::new();
    for i in (0..map.len()).step_by(2) {
        let id = i/2;
        for _ in 0..map[i] {
            seq.push(id as i32)
        }
        if i+1 < map.len() {
            for _ in 0..map[i+1] {
                seq.push(-1);
            }
        }
    }

    let mut ranges = HashMap::new();
    let mut i = 0;
    while i < seq.len() {
        if seq[i] == -1 { 
            i += 1;
            continue 
        }
        let mut j = i;
        while j < seq.len() && seq[j] == seq[i] {
            j += 1;
        }
        ranges.insert(seq[i], (i, j));
        i = j;
    }
    for v in (0..=*ranges.keys().max().unwrap()).rev() {
        let (i, j) = ranges.get(&v).unwrap();
        let mut k = 0;
        while k < *i {
            while k < *i && seq[k] != -1 {
                k += 1;
            }
            let mut l = k;
            while l < *i && seq[l] == -1 {
                l += 1;
            }
            if (j-i) <= (l-k) {
                for x in 0..(j-i) {
                    seq.swap(i+x, k+x);
                }
                break
            }
            k = l;
        }
    }

    let mut checksum = 0;
    for i in 0..seq.len() {
        if seq[i] == -1 { continue }
        checksum += seq[i] as usize * i;
    }
    println!("{}", checksum);
}
