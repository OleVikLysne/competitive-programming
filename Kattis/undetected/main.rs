use std::collections::HashSet;
fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let n: usize =  buf.trim().parse().unwrap();

    let mut boundary_circles = Vec::new();
    let mut circles = Vec::new();
    for i in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        let x = foo.next().unwrap();
        let y = foo.next().unwrap();
        let r = foo.next().unwrap();
        if x-r<0 {
            boundary_circles.push(i)
        }
        circles.push((x,y,r));
    }

    let mut g: Vec<Vec<usize>> = vec![Vec::new(); n];
    for i in 0..n {
        for j in i+1..n {
            if overlap(&circles[i], &circles[j]) {
                g[i].push(j);
                g[j].push(i)
            }
        }
    }

    let mut lower = 0;
    let mut upper = n;
    let mut mid = n>>1;
    while lower != mid {
        let mut visited = HashSet::new();
        let mut dummy = false;
        for c_idx in &boundary_circles {
            if c_idx >= &mid { break }
            let c = circles[*c_idx];
            if c.0 + c.2 > 200 || _path_blocked(&g, &circles, *c_idx, &mid, &mut visited) {
                dummy=true;
                break;
            }
        }
        if dummy { upper = mid }
        else { lower = mid }
        mid = (lower+upper)>>1;
    }
    println!("{}", mid);
}

fn _path_blocked(
    g: &Vec<Vec<usize>>,
    circles: &Vec<(i32, i32, i32)>,
    src: usize,
    k: &usize, 
    visited: &mut HashSet<usize>
) -> bool {
    visited.insert(src);
    for c_idx in &g[src] {
        if c_idx >= k { break }
        if visited.contains(c_idx) { continue }
        let c = &circles[*c_idx];
        if c.0 + c.2 > 200 || _path_blocked(g, circles, *c_idx, k, visited) {
            return true
        }
    }
    false
}

fn overlap(c1: &(i32,i32,i32), c2: &(i32,i32,i32)) -> bool {
    (c1.0-c2.0).pow(2) + (c1.1-c2.1).pow(2) < (c1.2+c2.2).pow(2)
}
