use std::collections::VecDeque;

fn main() -> Result<(), std::num::ParseIntError> {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse()?;
    let mut arr: Vec<u32> = Vec::new();
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        arr.push(buf.trim().parse()?);
    }

    let mut start = vec![0];
    for i in 1..n {
        if arr[i] >= arr[start[0]] {
            if arr[i] > arr[start[0]] {
                start.clear();
            }
            start.push(i);
        } 
    }

    let mut res = vec![-1; n];
    let mut m = vec![vec![usize::MAX; 2]; n];
    for i in (0..n).rev() {
        for j in i+1..n {
            if arr[j] > arr[i] {
                m[i][0] = j;
                break
            }
            let k = m[j][0];
            if k == usize::MAX || arr[k] > arr[i] {
                m[i][0] = k;
                break
            }

        }
    }
    
    for i in 0..n {
        for j in (0..i).rev() {
            if arr[j] > arr[i] {
                m[i][1] = j;
                break
            }
            let k = m[j][1];
            if k == usize::MAX || arr[k] > arr[i] {
                m[i][1] = k;
                break
            }

        }
    }

    let mut rev_m = vec![Vec::new(); n];
    for i in 0..n {
        for j in &m[i] {
            if *j != usize::MAX {
                rev_m[*j].push(i);
            }
        }
    }
    let mut q = VecDeque::new();
    for i in start.iter() {
        res[*i] = 0;
        q.push_back((*i, 0))
    }
    while let Some((i, c)) = q.pop_front() {
        for j in rev_m[i].iter() {
            if res[*j] == -1 {
                res[*j] = c+1;
                q.push_back((*j, c+1));
            }
        }
    }
    for x in res {
        print!("{} ", x);
    }
    Ok(())
}
