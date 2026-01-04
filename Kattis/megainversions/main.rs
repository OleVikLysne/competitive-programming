fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse().unwrap();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut offset: u64 = 0;
    let mut arr: Vec<u64> = Vec::with_capacity(n);
    for i in buf.split_whitespace().map(|x| x.parse::<u64>().unwrap()) {
        arr.push(i*(n as u64)+offset);
        offset+=1;
    }

    let mut sorted_arr = arr.clone();
    sorted_arr.sort_unstable();
    let mut output: Vec<u64> = vec![1; n];
    let mut tree: Vec<i32> = vec![0; n*2];

    for i in 0..n {
        let k = sorted_arr.binary_search(&arr[i]).unwrap()+n;
        output[i]*=query(&tree, k, n-1+n) as u64;
        update(&mut tree, k, 1);
    }
    tree.fill(0);
    for i in (0..n).rev() {
        let k = n-1-sorted_arr.binary_search(&arr[i]).unwrap()+n;
        output[i]*=query(&tree, k, n-1+n) as u64;
        update(&mut tree, k, 1);
    }
    println!("{}", output.iter().sum::<u64>());
}

fn update(tree: &mut [i32], mut i: usize, val: i32) {
    let diff = val-tree[i];
    if diff == 0 { return }
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