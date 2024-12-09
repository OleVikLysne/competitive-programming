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
    let mut i = seq.len()-1;
    let mut j = 0;
    while i > j {
        
        while seq[j] != -1 {
            j += 1
        }
        while i > j && seq[j] == -1 {
            if seq[i] == -1 {
                i -= 1;
                continue
            }
            seq.swap(i, j);
            i -= 1;
            j += 1;
        }
    }
    let mut checksum = 0;
    for i in 0..seq.len() {
        if seq[i] == -1 { break }
        checksum += seq[i] as usize * i;
    }
    println!("{}", checksum);
}