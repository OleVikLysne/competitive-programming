fn floyd_warshall(dist: &mut [Vec<i64>]) {
    let n = dist.len();
    for i in 0..n {
        dist[i][i] = 0;
    }
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if dist[i][j] < 0 { continue }
                if dist[k][j] < INF && dist[i][k] < INF && dist[i][j] > dist[i][k] + dist[k][j] {
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