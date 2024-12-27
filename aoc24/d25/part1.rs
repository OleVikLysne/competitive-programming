fn main() {
    let inp: Vec<Vec<char>> = std::io::stdin().lines().map(|x| x.unwrap().chars().collect()).collect();
    let mut keys = Vec::new();
    let mut locks = Vec::new();
    for k in (0..inp.len()).step_by(8) {
        let mut v = vec![-1; 5];
        for i in 0..7 {
            for j in 0..5 {
                if inp[k+i][j] == '#' {
                    v[j] += 1;
                }
            }
        }
        if inp[k][0] == '#' {
            keys.push(v)
        } else {
            locks.push(v);
        }
    }
    let mut total = 0;
    for key in keys {
        for lock in &locks {
            let mut broke = false;
            for i in 0..5 {
                if key[i] + lock[i] >= 6 {
                    broke = true;
                    break
                }
            }
            if !broke {total += 1}
        }
    }
    println!("{}", total);
}