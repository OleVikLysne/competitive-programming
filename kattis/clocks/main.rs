fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse().unwrap();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut clock1: [u32; 400_000] = [0; 400_000];
    let mut clock2: [u32; 400_000] = [0; 400_000];
    let mut lps: [u32; 200_000] = [0; 200_000];

    for (i, x) in buf.split_ascii_whitespace().map(|x| x.parse::<u32>().unwrap()).enumerate() {
        clock1[i] = x;
    }
    buf.clear();
    let _ = stdin.read_line(&mut buf);

    for (i, x) in buf.split_ascii_whitespace().map(|x| x.parse::<u32>().unwrap()).enumerate() {
        clock2[i] = x;
    }

    clock1[0..n].sort_unstable();
    clock2[0..n].sort_unstable();
    for i in 0..n-1 {
        clock1[i+n] = clock1[i+1]-clock1[i];
        clock2[i+n] = clock2[i+1]-clock2[i];
    }
    clock1[2*n-1] = clock1[0]+360_000-clock1[n-1];
    clock2[2*n-1] = clock2[0]+360_000-clock2[n-1];
    
    for i in 0..n {
        clock1[i] = clock1[i+n];
    }
    if kmp(&clock1[0..n*2], &clock2[n..2*n], &mut lps) {
        println!("possible")
    } else {
        println!("impossible")
    }
}

fn kmp(text: &[u32], pattern: &[u32], lps: &mut [u32]) -> bool {
    build_lps(pattern, lps);
    let mut i = 0;
    let mut j = 0;
    while i < text.len() {
        if text[i] == pattern[j] {
            i += 1;
            j += 1;
        }
        if j == pattern.len() {
            return true
        } 
        else if i < text.len() && text[i] != pattern[j] {
            if j != 0 {
                j = lps[j-1] as usize
            } else {
                i += 1
            }
        }
    }
    false
}

fn build_lps(pattern: &[u32], lps: &mut [u32]) {
    let mut length = 0;
    let mut i = 1;
    while i < pattern.len() {
        if pattern[i] == pattern[length] {
            length += 1;
            lps[i] = length as u32;
            i += 1;
        } else {
            if length != 0 {
                length = lps[length-1] as usize;
            } else {
                lps[i] = 0;
                i+= 1;
            }
        }
    }
}