fn tarjan(g: &[Vec<u32>]) -> Vec<Vec<u32>> {
    let n = g.len();

    let mut sccs = Vec::new();
    let mut on_stack = vec![false; n];
    let mut lowest = vec![u32::MAX; n];
    let mut pre_order = vec![u32::MAX; n];
    let mut count = 0;
    let mut stack = Vec::new();

    fn dfs(
        v: usize,
        prev: usize,
        g: &[Vec<u32>],
        sccs: &mut Vec<Vec<u32>>,
        on_stack: &mut [bool],
        lowest: &mut [u32],
        pre_order: &mut [u32],
        stack: &mut Vec<u32>,
        count: &mut u32,
    ) {
        stack.push(v as u32);
        lowest[v] = *count;
        pre_order[v] = *count;
        *count += 1;
        on_stack[v] = true;
        for u in g[v].iter().map(|u| *u as usize) {
            if u == prev { continue }
            if lowest[u] == u32::MAX {
                dfs(u, v, g, sccs, on_stack, lowest, pre_order, stack, count);
                lowest[v] = lowest[v].min(lowest[u]);
            } else if on_stack[u] {
                lowest[v] = lowest[v].min(lowest[u]);
            }
        }
        if lowest[v] == pre_order[v] {
            let mut scc = Vec::new();
            while let Some(u) = stack.pop() {
                on_stack[u as usize] = false;
                scc.push(u);
                if u == v as u32 {
                    break;
                }
            }
            sccs.push(scc);
        }
    }

    for v in 0..n {
        if pre_order[v] == u32::MAX {
            dfs(
                v,
                v,
                g,
                &mut sccs,
                &mut on_stack,
                &mut lowest,
                &mut pre_order,
                &mut stack,
                &mut count,
            );
        }
    }

    return sccs;
}
