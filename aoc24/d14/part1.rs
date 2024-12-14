
// const ROWS: i64 = 7;
// const COLS: i64 = 11;
const ROWS: i64 = 103;
const COLS: i64 = 101;

fn main() {
    let mut quads = vec![0; 4];
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut line_split = line.split_ascii_whitespace();
        let left = line_split.next().unwrap().trim_start_matches("p=");
        let right = line_split.next().unwrap().trim_start_matches("v=");
        
        let left: Vec<i64> = left.split(",").map(|x| x.parse().unwrap()).collect();
        let right: Vec<i64> = right.split(",").map(|x| x.parse().unwrap()).collect();
        let (mut i, mut j) = (left[1], left[0]);
        let (di, dj) = (right[1], right[0]);

        i += di*100;
        j += dj*100;
        i = i.rem_euclid(ROWS);
        j = j.rem_euclid(COLS);
        if i == ROWS/2 || j == COLS/2 { continue }
        let mut idx = 0;
        if i > ROWS/2 {
            idx += 1;
        }
        if j > COLS/2 {
            idx += 2;
        }
        quads[idx] += 1;
    }
    let mut prod = 1;
    for x in quads {
        prod *= x;
    }
    println!("{}", prod);
}