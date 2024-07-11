const COL_MAX: usize = 10_001;
const ROW_MAX: usize = 31;

fn main() {
    let mut pascal_triangle: [[u32; 31]; 31] = [[1; 31]; 31];
    for i in 1..31 {
        for j in 1..i {
            pascal_triangle[i][j] = pascal_triangle[i-1][j] + pascal_triangle[i-1][j-1];
        }
    }

    let mut tiles: [u16; 30] = [0; 30];
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let g: u8 = buf.trim().parse().unwrap();
    buf.clear();

    for i in 1..g+1 {
        let _ = stdin.read_line(&mut buf);
        let n: usize = buf.trim().parse().unwrap();
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        for (j, tile) in buf.split_whitespace().map(|x| x.parse::<u16>().unwrap()).enumerate() {
            tiles[j] = tile
        }
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace();
        let mut k: usize = foo.next().unwrap().parse().unwrap();
        let mut t: u16 = foo.next().unwrap().parse().unwrap();
        buf.clear();
        let s = tiles[0..n].iter().map(|x| *x as u32).sum::<u32>();
        if (t as u32+1) * (k as u32+1) > ((s - t as u32)+1)*((n-k) as u32+1) {
            k = n - k;
            t = s as u16 - t;
        }
        let mut dp: [u32; COL_MAX*ROW_MAX] = [0; COL_MAX*ROW_MAX];
        dp[0] = 1;
        let mut indices: Vec<Vec<u16>> = vec![Vec::new(); k+1];
        indices[0].push(0);
        let t_u = t as usize;
        for z in (0..n).rev() {
            let val = &tiles[z];
            let u = {
                if z >= k {
                    0
                } else {
                    k-z-1
                }
            };
            for i in (u..k).rev() {
                let (head, tail) = indices.split_at_mut(i+1);
                for j in &head[i] {
                    if j+val > t { continue }
                    if dp[(i+1)*(t_u+1)+(j+val) as usize] == 0 {
                        tail[0].push(j+val);
                    }
                    dp[(i+1)*(t_u+1)+(j+val) as usize] += dp[i*(t_u+1)+*j as usize];
                    
                }
            }
        }
        let w = dp[(k+1)*(t_u+1)-1];
        let n_choose_k = pascal_triangle[n][k];
        println!("Game {} -- {} : {}", i, w, n_choose_k-w);
    }
}