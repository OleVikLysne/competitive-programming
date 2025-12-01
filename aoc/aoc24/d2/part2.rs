fn not_safe(i: usize, j: usize, arr: &[i32], ord: bool) -> bool {
    if j >= arr.len() {
        return false
    }
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
        let mut count = 0;
        let mut i = 0;
        while i < n-1 {
            if not_safe(i, i+1, &arr, ord) {
                count += 1;
                if count == 2 {
                    break
                }
                let a = not_safe(i, i+2, &arr, ord);
                let b = not_safe(i+1, i+2, &arr, ord);
                if a && b {
                    count += 1;
                    break
                }
                if !a {
                    i += 1
                }
            }
            i += 1;
        }
        if count < 2 {
            s += 1;
        }
    }
    println!("{}", s);
}
