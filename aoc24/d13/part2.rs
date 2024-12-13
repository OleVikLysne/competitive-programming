use nalgebra::{Matrix2, Matrix2x1};

const ADD: f64 = 10000000000000.0;

fn main() {
    let mut total = 0;

    let lines: Vec<String> = std::io::stdin().lines().map(|x| x.unwrap()).collect();
    for i in (0..lines.len()).step_by(4) {
        let a = lines[i].trim_start_matches("Button A: ");
        let b = lines[i+1].trim_start_matches("Button B: ");
        let p = lines[i+2].trim_start_matches("Prize: ");

        let mut v: Vec<(f64, f64)> = Vec::new();
        for z in [a, b, p] {
            let mut foo = z.split_ascii_whitespace();
            let left = foo.next().unwrap().trim_start_matches("X").trim_start_matches("Y").trim_start_matches("=").trim_end_matches(",");
            let right = foo.next().unwrap().trim_start_matches("X").trim_start_matches("Y").trim_start_matches("=");
            println!("{} {}", left, right);
            v.push((left.parse().unwrap(), right.parse().unwrap()));
        }

        let (t_x, t_y) = v[2];
        let t_x = t_x + ADD;
        let t_y = t_y + ADD;
        let matrix = Matrix2::new(v[0].0, v[1].0, v[0].1, v[1].1);
        let vector = Matrix2x1::new(t_x, t_y);
        let res = matrix.try_inverse().unwrap() * vector;
        let mut res_int = Vec::new();
        for val in res.iter() {
            if (val.round() - val).abs() < 1e-3 {
                res_int.push(val.round() as u64);
            } else {break}
        }
        if res_int.len() == 2 {
            total += res_int[0]*3 + res_int[1];
        }    
    }

    println!("{}", total)
}