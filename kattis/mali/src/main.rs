fn main() -> Result<(), std::num::ParseIntError> {
    let mut a_occ = [0; 100];
    let mut b_occ = [0; 100];
    let mut a_list = [0; 100_000];
    let mut b_list = [0; 100_000];

    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse()?;

    for i in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_ascii_whitespace();
        let a: u8 = foo.next().unwrap().parse()?;
        let b: u8 = foo.next().unwrap().parse()?;
        sort_swap(&mut a_list, i, &mut a_occ, a);
        sort_swap(&mut b_list, i, &mut b_occ, b);
        print!("{} ", count(&a_list, &a_occ, &b_list, i));
    }
    Ok(())
}

fn sort_swap(arr: &mut [u8], mut i: usize, jump_arr: &mut [u32], val: u8) {
    arr[i] = val;
    while i > 0 && arr[i-1] >= val {
        let j = i - jump_arr[arr[i-1] as usize] as usize;
        arr.swap(i, j);
        i = j;
    }
    jump_arr[val as usize] += 1
}

fn count(arr: &[u8], jump_arr: &[u32], other_arr: &[u8], mut i: usize) -> u8 {
    let n = i+1;
    i = n - jump_arr[arr[n-1] as usize] as usize;
    let mut maxi = 0;
    loop {
        maxi = maxi.max(arr[i] + other_arr[n-i-1]);
        if i == 0 {
            break
        }
        i -= jump_arr[arr[i-1] as usize] as usize
    }
    maxi
}


