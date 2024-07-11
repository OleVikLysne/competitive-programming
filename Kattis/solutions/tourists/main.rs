const SIZE: usize = 200_001;
const MAX_LOG: usize = 18;


fn main() {
    let mut anc_matrix: [[u32; SIZE]; MAX_LOG] = [[0; SIZE]; MAX_LOG];
    let mut depth = [0; SIZE];

    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse().unwrap();

    let mut g: Vec<Vec<u32>> = vec![Vec::new(); n+1];
    for _ in 0..n-1 {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_ascii_whitespace();
        let i: u32 = foo.next().unwrap().parse().unwrap();
        let j: u32 = foo.next().unwrap().parse().unwrap();
        g[i as usize].push(j);
        g[j as usize].push(i);
    }
    compute_parent(0, 1, &g, &mut anc_matrix, &mut depth);

    let log_n = (usize::BITS-n.leading_zeros()) as usize;
    for i in 1..log_n {
        for j in 1..=n {
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j] as usize];
        }
    }
    
    let mut s: u64 = depth[2..=n].iter().map(|x| *x as u64).sum();

    for i in 2..=(n/2) {
        for j in (i*2..=n).step_by(i) {
            s += lca_path_search(i, j, &anc_matrix, &depth);
        }
    }
    println!("{}", s)
}


fn compute_parent(v: usize, u: usize, g: &[Vec<u32>], anc_matrix: &mut [[u32; SIZE]; MAX_LOG], depth: &mut [u32]) {
    depth[u] = depth[v] + 1;
    anc_matrix[0][u] = v as u32;
    for w in g[u].iter().map(|x| *x as usize) {
        if w != v {
            compute_parent(u, w, g, anc_matrix, depth)
        }
    }
}


fn anc(mut x: usize, k: &u32, anc_matrix: &[[u32; SIZE]; MAX_LOG]) -> usize {
    for j in (0..MAX_LOG).rev() {
        if k & (1 << j) != 0 {
            x = anc_matrix[j][x] as usize;
        }
     }
    return x
}

fn lca_path_search(mut u: usize, mut v: usize, anc_matrix: &[[u32; SIZE]; MAX_LOG], depth: &[u32]) ->  u64 {
    if depth[v] > depth[u] {
        std::mem::swap(&mut u, &mut v);
    }
    let mut diff = depth[u]-depth[v];
    if diff > 0 {
        u = anc(u, &diff, anc_matrix);
    }
    if u == v {
        return (diff+1) as u64;
    }
    
    let log_n = (u32::BITS - depth[v].leading_zeros()-1) as usize;
    for i in (0..=log_n).rev() {
        if anc_matrix[i][u] != anc_matrix[i][v] {
            u = anc_matrix[i][u] as usize;
            v = anc_matrix[i][v] as usize;
            diff += 1 << (i+1);
        }
    }
    return (diff+3) as u64
}