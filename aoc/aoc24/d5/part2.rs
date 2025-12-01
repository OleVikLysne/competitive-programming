use std::collections::HashSet;

fn topological_sort(g: &Vec<Vec<usize>>, arr: &[usize]) -> Option<Vec<usize>> {
    let n = g.len();
    let mut in_deg = vec![0; n];
    let arr_set: HashSet<usize> = arr.iter().cloned().collect();
    for i in arr {
        for j in &g[*i] {
            in_deg[*j] += 1;
        }
    }

    let mut roots = Vec::new();
    for i in 0..n {
        if in_deg[i] == 0 && arr_set.contains(&i) {
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
        arr_set: &HashSet<usize>
    ) -> bool {
        if rec_visited[v] {
            return false;
        }
        if !visited[v] {
            visited[v] = true;
            rec_visited[v] = true;

            for u in &g[v] {
                if !arr_set.contains(u) {
                    continue
                }
                if !dfs(*u, g, rec_visited, visited, topo_order, arr_set) {
                    return false;
                }
            }
            rec_visited[v] = false;
            topo_order.push(v)
        }
        return true;
    }

    for root in roots {
        if !dfs(root, g, &mut rec_visited, &mut visited, &mut topo_order, &arr_set) {
            return None;
        }
    }
    topo_order.reverse();
    Some(topo_order)
}

fn main() {
    let stdin = std::io::stdin();
    let mut g = vec![Vec::new(); 100];
    let mut buf = String::new();
    loop {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        if buf.trim().len() == 0 {
            break
        }
        let mut foo = buf.trim().split("|");
        let v: usize = foo.next().unwrap().parse().unwrap();
        let u: usize = foo.next().unwrap().parse().unwrap();
        g[v].push(u);
    }

    
    let mut total = 0;
    for line in stdin.lines() {
        let line = line.unwrap();
        let arr: Vec<usize> = line.split(",").map(|x| x.parse::<usize>().unwrap()).collect();
        let mut valid = true;
        for i in 1..arr.len() {
            if !g[arr[i-1]].contains(&arr[i]) {
                valid = false;
                break
            }
        }
        if !valid {
            let topo_order = topological_sort(&g, &arr).unwrap();
            total += topo_order[topo_order.len()/2]
        }
    }
    println!("{}", total);
}
