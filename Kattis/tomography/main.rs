fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut String::new());
    let _ = stdin.read_line(&mut buf);
    let rows: Vec<i32> = buf.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut cols: Vec<i32> = buf.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    if rows.iter().sum::<i32>() != cols.iter().sum::<i32>() {
        println!("No");
        return
    }
    for n in rows {
        cols.sort_unstable_by(|a,b| b.cmp(a));
        for i in 0..n as usize {
            cols[i] -= 1;
            if cols[i] == -1 {
                println!("No");
                return
            }
        }
    }
    println!("Yes")
}
