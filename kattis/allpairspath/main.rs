const INF: i32 = 1000000;

fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    loop {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_ascii_whitespace();
        let n: usize = foo.next().unwrap().parse().unwrap();
        let m: usize = foo.next().unwrap().parse().unwrap();
        let q: u16 = foo.next().unwrap().parse().unwrap();
        if n == 0 && m == 0 && q == 0 { break }
        let mut dist = vec![vec![INF; n]; n];
        for i in 0..n {
            dist[i][i] = 0;
        }
        for _ in 0..m {
            buf.clear();
            let _ = stdin.read_line(&mut buf);
            let mut foo = buf.split_ascii_whitespace();
            let u: usize = foo.next().unwrap().parse().unwrap();
            let v: usize = foo.next().unwrap().parse().unwrap();
            let w: i32 = foo.next().unwrap().parse().unwrap();
            if w < dist[u][v] {
                dist[u][v] = w;
            }
        }
        floyd_warshall(&mut dist);
        for _ in 0..q {
            buf.clear();
            let _ = stdin.read_line(&mut buf);
            let mut foo = buf.split_ascii_whitespace();
            let u: usize = foo.next().unwrap().parse().unwrap();
            let v: usize = foo.next().unwrap().parse().unwrap();
            let d = dist[u][v];
            if d == INF {
                println!("Impossible")
            } else if d == -INF {
                println!("-Infinity");
            } else {
                println!("{}", d);
            }
        }
        println!()
    }
}

fn floyd_warshall(dist: &mut [Vec<i32>]) {
    let n = dist.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if dist[i][j] < 0 { continue }
                if dist[i][j] > dist[i][k] + dist[k][j] && dist[i][k] < INF && dist[k][j] < INF {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    for i in 0..n {
        for j in 0..n {
            for k in 0..n {
                if dist[k][k] < 0 && dist[i][k] != INF && dist[k][j] != INF {
                    dist[i][j] = -INF;
                    break
                }
            }
        }
    }
}