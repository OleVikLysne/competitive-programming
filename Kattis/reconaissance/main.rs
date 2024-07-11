fn get_pos(car: &(f64, f64), t: &f64) -> f64 {
    return car.0 + car.1*t;
}

fn dist(cars: &Vec<(f64, f64)>, t: &f64) -> f64 {
    let mut min: f64 = f64::MAX;
    let mut max: f64 = f64::MIN;
    for car in cars {
        let pos = get_pos(&car, t);
        min = f64::min(pos, min);
        max = f64::max(pos, max);
    }
    return max-min;
}

fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n = buf.split_whitespace().map(|x| x.parse::<usize>().unwrap()).next().unwrap();
    let mut cars: Vec<(f64, f64)> = Vec::with_capacity(n);
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace().map(|x| x.parse::<f64>().unwrap());
        cars.push((foo.next().unwrap(), foo.next().unwrap()));
    }

    let mut upper_bound: f64 = 200000.0;
    let mut lower_bound: f64 = 0.0;
    let epsilon: f64 = 0.0005;
    loop {
        let mid = (upper_bound + lower_bound)/2.0;
        if  upper_bound-lower_bound < epsilon {
            println!("{}", dist(&cars, &mid));
            break;
        }
        if dist(&cars, &mid) < dist(&cars, &(mid+epsilon)) {
            upper_bound = mid;
        }
        else {
            lower_bound = mid;
        }
    }
}
