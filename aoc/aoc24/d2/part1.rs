fn not_safe(i: usize, j: usize, arr: &[i32], ord: bool) -> bool {
    return arr[i] == arr[j] || (arr[i] < arr[j]) != ord || (arr[i]-arr[j]).abs() > 3
}

fn main() {
    let stdin = std::io::stdin();
    let mut s = 0;
    for line in stdin.lines().map(|x| x.unwrap()) {
        let arr: Vec<i32> = line.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        let n = arr.len();
        if n == 1 {
            s += 1;
            continue
        }
        let ord = arr[0] < arr[1];
        let mut dummy = false;
        for i in 0..n-1 {
            if not_safe(i, i+1, &arr, ord) {
                dummy = true;
                break
            }
        }
        if !dummy {
            s += 1;
        }
    }
    println!("{}", s);
}
