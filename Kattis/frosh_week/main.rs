fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse().unwrap();
    let mut s: Vec<u32> = vec![0; 2*n];
        for e in &mut s[0..n] {
            buf.clear();
            let _ = stdin.read_line(&mut buf);
            *e = buf.trim().parse().unwrap();
        }
    println!("{}", merge_sort(&mut s, 0, n, &n));
}

fn merge_sort(arr: &mut [u32], l: usize, r: usize, n: &usize) -> usize {
    let mut count = 0;
    let mid = (l+r)>>1;
    if r-l > 2 {
        count += merge_sort(arr, l, mid, &n);
        count += merge_sort(arr, mid, r, &n);
    }
    let mut i = l;
    let mut j = mid;
    let mut k = l+n;

    while i<mid && j<r {
        if arr[i]<=arr[j] {
            arr[k] = arr[i];
            i+=1;
            k+=1;
        }
        else {
            arr[k] = arr[j];
            count += mid-i;
            j+=1;
            k+=1;
        }
    }

    arr.copy_within(i..mid, k);
    k+=mid-i;
    arr.copy_within(j..r, k);
    arr.copy_within(l+n..r+n, l);
    count
}