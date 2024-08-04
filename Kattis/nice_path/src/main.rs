// 62 / 100

type T = (u64, u32, u64, u32);

fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let mut nm = buf.split_ascii_whitespace();
    let n: usize = nm.next().unwrap().parse().unwrap();
    let m: usize = nm.next().unwrap().parse().unwrap();
    buf.clear();
    let mut g: Vec<Vec<(usize, u64)>> = vec![Vec::new(); n];

    for _ in 0..m {
        let _ = stdin.read_line(&mut buf);
        let mut uvw = buf.split_ascii_whitespace();
        let u: usize = uvw.next().unwrap().parse().unwrap();
        let v: usize = uvw.next().unwrap().parse().unwrap();
        let w: u64 = uvw.next().unwrap().parse().unwrap();
        g[u-1].push((v-1, w));
        buf.clear();
    }
    for i in 0..n {
        g[i].sort_unstable();
    }

    let mut mem: Vec<T> = vec![(u64::MAX, 1, 1, 1); n];
    let res = search(0, 0, 0, &g, &mut mem, &n);
    let a = res.0 as f64;
    let b = res.1 as f64;
    println!("{}", a/b);
}

fn search(v: usize, collected: u64, visit_count: u32, g: &Vec<Vec<(usize, u64)>>, mem: &mut [T], n: &usize) -> (u64, u32) {
    if v == n-1 {
        return (collected, visit_count);
    }
    if mem[v].0 != u64::MAX {
        let pre_collect = &mem[v].0;
        let pre_count = &mem[v].1;
        let post_collect = &mem[v].2;
        let post_count = &mem[v].3;
        let stored_score = (pre_collect+post_collect) * (visit_count+post_count) as u64;
        let new_score = (collected+post_collect) * (pre_count+post_count) as u64;
        if new_score < stored_score {
            return (pre_collect+post_collect, pre_count+post_count)
        }
    }

    let mut best = mem[v];
    let mut stored_score = -1.0;
    for (u, w) in g[v].iter() {
        let res = search(*u, collected+w, visit_count+1, g, mem, n);
        let coll = &res.0;
        let count = &res.1;
        let score = *coll as f64 / *count as f64;
        if score > stored_score {
            best = (collected, visit_count, coll-collected, count-visit_count);
            stored_score = score;
        }
    }
    mem[v] = best;
    return (best.0+best.2, best.1+best.3);
}
