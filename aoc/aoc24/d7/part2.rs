fn add(x: i64, y: i64) -> i64 {
    x+y
}
fn mul(x: i64, y: i64) -> i64 {
    x*y
}

fn conc(x: i64, y: i64) -> i64 {
    let mut x = x.to_string();
    x.extend(y.to_string().chars());
    x.parse().unwrap()
}

const OPS: [fn(i64, i64) -> i64; 3] = [add, mul, conc];

fn search(arr: &[i64], target: i64, i: usize, tot: i64) -> bool {
    if i == arr.len() {
        if tot == target {
            return true
        }
        return false
    }

    for op in OPS {
        if search(arr, target, i+1, op(tot, arr[i])) {
            return true
        }
    }
    false
}

fn main() {
    let mut total = 0;
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut foo = line.split_ascii_whitespace();
        let mut target = foo.next().unwrap().to_string();
        target.pop();
        let target: i64 = target.parse().unwrap();
        let arr: Vec<i64> = foo.map(|x| x.parse().unwrap()).collect();
        if search(&arr, target, 1, arr[0]) {
            total += target as i64;
        }
    }
    println!("{}", total)
}