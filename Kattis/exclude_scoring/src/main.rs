use std::num::ParseIntError;
const SCORE_MAP: [u32; 30] = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7,6, 5, 4, 3, 2, 1];

fn main() -> Result<(), ParseIntError> {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut nm = buf.split_ascii_whitespace();
    let n: u8 = nm.next().unwrap().parse()?;
    let m: u32 = nm.next().unwrap().parse()?;
    let k = 4.min(n - 1);

    let our_score: u16 = next_agg(&stdin, &mut buf, &mut [0; 9])?.iter().sum();
    let mut worst_rank: u32 = 1;
    let mut diffs: [u16; 99999] = [0; 10usize.pow(5)-1];
    let mut n = 0;
    for _ in 0..m-1 {
        let mut temp = [0; 9];
        let agg = next_agg(&stdin, &mut buf, &mut temp)?;
        let mut score: u16 = agg.iter().sum();
        if score > our_score {
            worst_rank += 1;
            continue
        }
        if k >= 4 {
            score -= agg.iter().min().unwrap()
        }
        if score + 100 < our_score {
            continue
        }
        diffs[n] = our_score - score;
        n += 1
    }
    diffs[..n].sort_unstable();

    let mut lower = 0;
    let mut upper = (n + 1) as u32;
    while upper - lower > 1 {
        let mid = (lower + upper) / 2;
        let mut total = 0;
        let mut c = 0;
        for (i, diff) in diffs[..mid as usize].iter().enumerate().map(|(i, x)| (i as u32, x)) {
            total += get_score(mid - i - 1);
            c += 1;
            if total.div_ceil(c) as u16 > *diff {
                total = 0;
                c = 0;
            }
        }
        if c == 0 {
            lower = mid
        } else {
            upper = mid
        }
    }
    print!("{}", worst_rank + lower);
    Ok(())
}

fn next_agg<'a>(
    stdin: &std::io::Stdin,
    buf: &mut String,
    temp: &'a mut [u16; 9],
) -> Result<&'a [u16], ParseIntError> {
    buf.clear();
    let _ = stdin.read_line(buf);
    for (i, x) in buf.split_ascii_whitespace().enumerate() {
        temp[i] = x.parse()?;
    }
    temp.select_nth_unstable(5);
    Ok(&temp[5..])
}

fn get_score(i: u32) -> u32 {
    match SCORE_MAP.get(i as usize) {
        Some(v) => return 1+*v,
        None => return 1
    }
}