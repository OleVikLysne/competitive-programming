fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut info = buf.split_whitespace();
    
    let n = info.next().unwrap().parse::<usize>().unwrap();
    let k = info.next().unwrap().parse::<u32>().unwrap();
    let mut event_starts: Vec<u32> = Vec::with_capacity(n);
    let mut event_ends: Vec<u32> = Vec::with_capacity(n);
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut line = buf.split_whitespace().map(|x| x.parse::<u32>().unwrap());
        event_starts.push(line.next().unwrap());
        event_ends.push(line.next().unwrap()+k);
    }
    event_starts.sort_unstable();
    event_ends.sort_unstable();
    

    let mut count: u32 = 0;
    let mut max_count: u32 = 0;
    let mut i: usize = 0;
    let mut j: usize = 0;
    while i<n {
        if event_starts[i] <= event_ends[j] {
            count += 1;
            i+=1;
            max_count = std::cmp::max(max_count, count);
        }
        else {
            count -= 1;
            j+=1;
        }
    }
    println!("{}", max_count);
}
