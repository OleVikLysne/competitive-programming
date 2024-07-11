#[allow(non_snake_case)] 
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut foo = buf.split_whitespace();
    let n: usize = foo.next().unwrap().parse().unwrap();
    let q: u32 = foo.next().unwrap().parse().unwrap();
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    let mut V: Vec<u64> = buf.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut gems: Vec<u8> = buf.trim().chars().map(|x| (x.to_digit(10).unwrap()-1) as u8).collect();
    buf.clear();

    let mut trees = vec![vec![0; 2*n]; 6];

    for (k, tree) in trees.iter_mut().enumerate() {
        for (i, g) in gems.iter().enumerate() {
            tree[i+n] = (k as u8 == *g) as i32;
        }
    }

    // build trees
    for tree in &mut trees {
        for i in (1..n).rev() {
            tree[i] = tree[2*i] + tree[2*i+1];
        }
    }

    for _ in 0..q {
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace();
        let a = foo.next().unwrap();

        if a == "1" {
            let k: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let p: u8 = foo.next().unwrap().parse::<u8>().unwrap()-1;
            let old_p = gems[k] as usize;
            update(&mut trees[old_p], k+n, 0);
            update(&mut trees[p as usize], k+n, 1);
            gems[k] = p;
        }

        else if a == "2" {
            let p: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let v: u64 = foo.next().unwrap().parse().unwrap();
            V[p] = v;
        }

        else if a == "3" {
            let l: usize = foo.next().unwrap().parse::<usize>().unwrap()+n-1;
            let r: usize = foo.next().unwrap().parse::<usize>().unwrap()+n-1;
            let mut s: u64 = 0;
            for (i, tree) in trees.iter().enumerate() {
                s += (query(&tree, l, r) as u64) * V[i];
            }
            println!("{}", s);
        }
        buf.clear();
    }


}

fn update(tree: &mut [i32], mut i: usize, val: i32) {
    let diff = val-tree[i];
    tree[i] = val;
    while i>1 {
        i = i>>1;
        tree[i] += diff;
    }
}

fn query(tree: &[i32], mut l: usize, mut r: usize) -> i32 {
    if l == r {
        return tree[l];
    }
    let mut s = tree[l] + tree[r];
    loop {
        let pl = l>>1;
        let pr = r>>1;
        if pl == pr { return s }
        if l % 2 == 0 {
            s+=tree[l+1];
        }
        if r % 2 == 1 {
            s+=tree[r-1];
        }
        l = pl;
        r = pr;
    }
}
