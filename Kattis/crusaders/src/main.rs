use std::io::Write;


fn main() {
unsafe {
    let mut arr = [0; 10_usize.pow(6)+2];
    
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut foo = buf.split_ascii_whitespace();
    let c: usize = foo.next().unwrap_unchecked().parse().unwrap_unchecked();
    arr[c+1] = 10_u32.pow(9)+1;

    let mut buf2 = String::new();
    let mut res: Vec<u32> = Vec::new();

    buf.clear();
    let _ = stdin.read_line(&mut buf);
    for val in buf.split_ascii_whitespace().map(|x| x.parse::<u32>().unwrap_unchecked()) {
        let mut lower = 0;
        let mut upper = c+2;
        while lower + 1 < upper {
            let mid = (lower+upper)/2;
            if arr[mid] == 0 {
                println!("Q {}", mid);
                let _ = std::io::stdout().flush();
                buf2.clear();
                let _ = stdin.read_line(&mut buf2);
                arr[mid] = buf2.trim().parse().unwrap_unchecked();
            }
            if arr[mid] <= val {
                lower = mid;
                if arr[mid] == val {
                    break
                }
            } else {
                upper = mid
            }
        }
        res.push(lower as u32);
    }
    print!("A ");
    res.iter().for_each(|x| print!("{} ", x));
}
}
