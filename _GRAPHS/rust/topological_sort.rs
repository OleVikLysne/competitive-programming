// NOT TESTED

fn topological_sort(g: &Vec<Vec<usize>>) -> Option<Vec<usize>> {
    let n = g.len();
    let mut in_deg = vec![0; n];
    for i in 0..n {
        for j in &g[i] {
            in_deg[*j] += 1;
        }
    }

    let mut roots = Vec::new();
    for i in 0..n {
        if in_deg[i] == 0 {
            roots.push(i);
        }
    }

    if roots.len() == 0 {
        return None;
    }

    let mut topo_order = Vec::new();
    let mut visited = vec![false; n];
    let mut rec_visited = vec![false; n];

    fn dfs(
        v: usize,
        g: &Vec<Vec<usize>>,
        rec_visited: &mut [bool],
        visited: &mut [bool],
        topo_order: &mut Vec<usize>,
    ) -> bool {
        if rec_visited[v] {
            return false;
        }
        if !visited[v] {
            visited[v] = true;
            rec_visited[v] = true;

            for u in &g[v] {
                if !dfs(*u, g, rec_visited, visited, topo_order) {
                    return false;
                }
            }
            rec_visited[v] = false;
            topo_order.push(v)
        }
        return true;
    }

    for root in roots {
        if !dfs(root, g, &mut rec_visited, &mut visited, &mut topo_order) {
            return None;
        }
    }
    topo_order.reverse();
    Some(topo_order)
}