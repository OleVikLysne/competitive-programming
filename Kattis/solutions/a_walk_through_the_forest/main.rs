use std::collections::BinaryHeap;
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::with_capacity(20);
    let mut pq: BinaryHeap<(u32, u16)> = BinaryHeap::new();
    let mut dist: [u32; 1000] = [u32::MAX-1000001; 1000];
    loop {
        let _ = stdin.read_line(&mut buf);
        if buf.starts_with("0") {break}
        let mut nm = buf.split_whitespace();
        let n: usize = nm.next().unwrap().parse().unwrap();
        let m: usize = nm.next().unwrap().parse().unwrap();
        buf.clear();

        let mut g: Vec<Vec<(u16, u32)>> = vec![Vec::new(); n];
        for _ in 0..m {
            let _ = stdin.read_line(&mut buf);
            let mut uvw = buf.split_whitespace();
            let u: u16 = uvw.next().unwrap().parse().unwrap();
            let v: u16 = uvw.next().unwrap().parse().unwrap();
            let w: u32 = uvw.next().unwrap().parse().unwrap();
            g[(u-1) as usize].push((v-1, w));
            g[(v-1) as usize].push((u-1, w));
            buf.clear();
        }
        // dijkstra
        dist[1] = 0;
        pq.push((0, 1));
        while pq.len() > 0 {
            let (_, u) = pq.pop().unwrap();
            for (v, w) in &g[u as usize] {
                let alt = dist[u as usize]+w;
                if dist[*v as usize] > alt {
                    dist[*v as usize] = alt;
                    pq.push((alt, *v));
                }
            }
        }
        let mut cache: Vec<i32> = vec![-1; n];
        path_search(0, &1, &g, &dist, &mut cache);
        println!("{}", cache[0]);
        dist.fill(u32::MAX-1000001)
    }
}

fn path_search(
s: usize, 
t: &u16, 
g: &Vec<Vec<(u16, u32)>>, 
dist: &[u32; 1000],
cache: &mut Vec<i32>
)  {
    let mut paths: i32 = 0;
    for (v, _) in &g[s] {
        if v == t {
            paths += 1;
            continue
        }
        let v = *v as usize;
        if &dist[v] < &dist[s] {
            if cache[v] == -1 {
                path_search(v, t, g, dist, cache)
            }
                paths += cache[v];
        }
    }
    cache[s] = paths;
}