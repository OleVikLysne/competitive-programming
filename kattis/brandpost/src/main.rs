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
    let mut unreachable = Vec::new();
    for i in 0..h {
        let mut reachable = Vec::new();
        let ii = i as i16;
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
            while let Some((x, y)) = unreachable.pop() {
                let d = steps - manhattan_dist(&ii, &ji, &x, &y);
                if d <= 0 {
                    unreachable.push((x, y));
                    break 
                }
                board[i][j] += d as u64;
                reachable.push(-y);
            }
        }
        unreachable.clear();
    }
    for i in (0..h-1).rev() {
        board[i][0] += board[i+1][0];
    }
    for j in 1..w {
        board[h-1][j] += board[h-1][j-1];
    }
    
    for i in (0..h-1).rev() {
        for j in 1..w {
            board[i][j] += board[i+1][j].min(board[i][j-1])
        }
    }
    print!("{}", board[0][w-1]);
    Ok(())
}

fn manhattan_dist(i: &i16, j: &i16, x: &i16, y:&i16) -> i16 {
    return (i-x).abs() + (j-y).abs()
}