fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let iterations: u8 = buf.trim().parse().unwrap();
    let mut henchmen: [(i16, f32); 16] = [(0, 0.0); 16];
    let mut mem: [[f32; 2_usize.pow(16)]; 17] = [[-1.0; 2_usize.pow(16)]; 17];
    for x in 0..iterations {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_ascii_whitespace(); 
        let n: u8 = foo.next().unwrap().parse().unwrap();
        let c: usize = foo.next().unwrap().parse().unwrap();
        let m: i16 = foo.next().unwrap().parse().unwrap();
        let mut z: usize = 0;
        for _ in 0..n {
            buf.clear();
            let _ = stdin.read_line(&mut buf);
            let mut foo = buf.split_ascii_whitespace();
            let cost: i16 = foo.next().unwrap().parse().unwrap();
            let prob: f32 = foo.next().unwrap().parse().unwrap();
            if cost <= m && prob > 0.0 {
                henchmen[z] = (cost, prob / 100.0);
                z += 1
            }
        }
        println!("{}", search(c, m, 0, 0, &henchmen, &z, &mut mem));
        if x+1 < iterations {
            for row in &mut mem[0..c+1] {
                for val in &mut row[0..2_usize.pow(z as u32)] {
                    *val = -1.0;
                }
            }
        }
    }
}

fn search(c: usize, m: i16, visited: usize, visited_count: usize, henchmen: &[(i16, f32)], num_henchmen: &usize, mem: &mut [[f32; 2_usize.pow(16)]; 17]) -> f32 {
    if mem[c][visited] != -1.0 {
        return mem[c][visited]
    }

    if m < 0 || (num_henchmen-visited_count) < c {
        return 0.0
    }
    if c == 0 {
        return 1.0
    }
    let mut res: f32 = 0.0;

    for j in 0..*num_henchmen {
        if visited & 1 << j != 0 { continue }
        let new_visited = visited | 1 << j;
        let cost = &henchmen[j].0;
        let prob = &henchmen[j].1;
        let total = 
            prob       * search(c-1, m-cost, new_visited, visited_count+1, henchmen, num_henchmen, mem) +
            (1.0-prob) * search(c, m-cost, new_visited, visited_count+1, henchmen, num_henchmen, mem);
        
        if total > res {
            res = total;
        }
    }

    mem[c][visited] = res;
    return res
}