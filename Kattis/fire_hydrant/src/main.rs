use std::num::ParseIntError;
use std::collections::BinaryHeap;

const N: usize = 1000;

fn main() -> Result<(), ParseIntError> {
    let mut board = [[0; N]; N];
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let mut whn = buf.trim().split_ascii_whitespace();
    let w: usize = whn.next().unwrap().parse()?;
    let h: usize = whn.next().unwrap().parse()?;
    let hi = h as i16;
    let wi = w as i16;
    let n: u32 = whn.next().unwrap().parse()?;
    let mut leaks = Vec::new();
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut ab = buf.trim().split_ascii_whitespace();
        let a: i16 = ab.next().unwrap().parse()?;
        let b: i16 = ab.next().unwrap().parse()?;
        let x = hi - b;
        let y = a - 1;
        leaks.push((x, y));
    }
    for i in 0..h {
        let ii = i as i16;
        let mut reachable = Vec::new();
        let mut unreachable = Vec::new();
        let steps = (hi-ii).abs();
        for (x, y) in &leaks {
            let d = steps - (ii-x).abs()-y;
            if d > 0 {
                board[i][0] += d as u64;
                reachable.push(-*y);
            } else if manhattan_dist(x, y, &ii, &wi) < wi+hi-ii {
                unreachable.push((*x, *y));
            }
        }
        let mut reachable = BinaryHeap::from(reachable);

        unreachable.sort_unstable_by_key(|x| -(ii-x.0).abs()-x.1);
        for j in 1..w {
            let ji = j as i16;
            while let Some(v) = reachable.peek() {
                if -v >= ji {
                    break
                }
                reachable.pop();
            }
            let right = reachable.len() as u64;
            board[i][j] = board[i][j-1] + right*2;
            let steps = (ii-hi).abs() + ji;
            while unreachable.len() > 0 {
                let (x, y) = &unreachable[unreachable.len()-1];
                let d = steps - manhattan_dist(&ii, &ji, x, y);
                if d <= 0 { 
                    break 
                }
                board[i][j] += d as u64;
                reachable.push(-y);
                unreachable.pop();
            }
        }
    }

    for step in 1..wi+hi-1 {
        for (x, y) in quarter_ring(step, hi-1, 0, &wi, &hi) {
            let xu = x as usize;
            let yu = y as usize;
            let mut val = u64::MAX;
            if valid(&(x+1), &y, &wi, &hi) {
                val = val.min(board[xu + 1][yu]);
            }
            if valid(&x, &(y-1), &wi, &hi) {
                val = val.min(board[xu][yu - 1]);
            }
            board[xu][yu] += val;
        }
    }
    print!("{}", board[0][w-1]);
    Ok(())
}


fn quarter_ring(
    mut step: i16,
    mut x: i16,
    mut y: i16,
    wi: &i16,
    hi: &i16
) -> Vec<(i16, i16)> {
    adjust(&mut step, &mut x, &mut y, wi);
    let mut l = Vec::new();
    for _ in 0..step {
        if !valid(&x, &y, wi, hi) {
            break
        }
        l.push((x, y));
        x -= 1;
        y -= 1;
    }
    if valid(&x, &y, wi, hi) {
        l.push((x, y))
    }
    return l
}

fn valid(x: &i16, y: &i16, wi: &i16, hi: &i16) -> bool {
    return !(x < &0 || x >= hi || y < &0 || y >= wi)
}

fn adjust(step: &mut i16, x: &mut i16, y: &mut i16, wi: &i16) {
    *y += *step;
    let y_dist = *y-wi+1;
    if y_dist > 0 {
        *step -= y_dist;
        *y -= y_dist;
        *x -= y_dist;
    }
}

fn manhattan_dist(i: &i16, j: &i16, x: &i16, y:&i16) -> i16 {
    return (i-x).abs() + (j-y).abs()
}