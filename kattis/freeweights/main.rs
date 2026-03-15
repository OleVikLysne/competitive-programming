use std::num::ParseIntError;
use std::collections::HashSet;
use std::cmp::max;

fn compute_cost(row: &mut Vec<u32>) -> u32 {
    let mut k = 1;
    let mut cost = 0;
    while k < row.len() {
        let i = row[k-1];
        let j = row[k];
        if i == j {
            k+=2;
            continue
        }
        else if i < j {
            cost = max(i, cost);
            k+=1;
        }
        else {
            cost = max(j, cost);
            row[k] = i;
            k+=1;
        }
    }
    return cost;
}
fn main() -> Result<(), ParseIntError> {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let n: u32 = buf.trim().parse()?;
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut top_row: Vec<u32> = buf
                            .split_whitespace()
                            .map(|x| x.parse::<u32>().unwrap())
                            .collect();
    if n == 1 {
        println!("{}", top_row[0]);
        return Ok(());
    } 
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut bottom_row: Vec<u32> = buf
                                        .split_whitespace()
                                        .map(|x| x.parse::<u32>().unwrap())
                                        .collect();

    let mut solo: HashSet<u32> = HashSet::new();
    for x in &bottom_row {
        if !solo.insert(*x) {
            solo.remove(x);
        }
    }
    let mut cost = match solo.iter().max() {
        None => 0,
        Some(c) => *c
    };
    cost = cost.max(compute_cost(&mut bottom_row)).max(compute_cost(&mut top_row));
    println!("{}", cost);
    Ok(())
}