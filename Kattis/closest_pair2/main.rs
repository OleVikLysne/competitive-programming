use std::io::BufRead;

#[derive(Copy)]
#[derive(Clone)]
struct Point {
    x: i64,
    y: i64,
}

fn main() {
    let stdin = std::io::stdin();
    let mut stdin = stdin.lock();
    let mut buf = Vec::with_capacity(20);
    let mut points = [Point{x: 0, y: 0}; 100000];
    let mut strip = [Point{x: 0, y: 0}; 100000];
    loop {
        let _ = stdin.read_until(b'\n', &mut buf);
        //trim_inp(&mut buf);
        buf.pop();
        let n = parse_inp(&buf) as usize / 100;
        if n == 0 { return }
        buf.clear();
        for i in 0..n {
            let _ = stdin.read_until(b'\n', &mut buf);
            //trim_inp(&mut buf);
            buf.pop();
            let mut line = buf.split(|x| *x==b' ');
            let x = parse_inp(line.next().unwrap());
            let y = parse_inp(line.next().unwrap());
            buf.clear();
            points[i] = Point{x, y};
        }
        points[0..n].sort_by(|a, b| a.x.cmp(&b.x));
        let res = closest_pair(&points[0..n], &mut strip[0..n]);
        let point1 = &res.1.0;
        let point2 = &res.1.1;
        let x1 = point1.x as f32 / 100.0;
        let y1 = point1.y as f32 / 100.0;
        let x2 = point2.x as f32 / 100.0;
        let y2 = point2.y as f32 / 100.0;

        println!("{:.2} {:.2} {:.2} {:.2}", x1, y1, x2, y2);
    }
}

fn closest_pair(points: &[Point], strip: &mut [Point]) -> (i64, (Point, Point)) {
    if points.len() <= 4 {
        return brute_force(points);
    }
    let mid = points.len()/2;
    let l = closest_pair(&points[..mid], strip);
    let r = closest_pair(&points[mid..], strip);
    let mut d;
    let mut closest;
    if l.0 < r.0 {
        d = l.0;
        closest = l.1;
    } else {
        d = r.0;
        closest = r.1;
    }

    let mid_x = points[mid].x;
    
    let mut n = 0;
    for e in &points[mid..] {
        if (e.x-mid_x).pow(2) <= d {
            strip[n] = *e;
            n += 1
        } else {
            break
        }
    }

    for e in points[..mid].iter().rev() {
        if (e.x-mid_x).pow(2) <= d {
            strip[n] = *e;
            n += 1
        } else {
            break
        }
    }

    strip[0..n].sort_by(|a, b| a.y.cmp(&b.y));
    for (i, vec1) in strip[..n-1].iter().enumerate() {
        for vec2 in &strip[i+1..(i+3).min(n)] {
            if (vec2.y - vec1.y).pow(2) >= d {
                break
            }
            let distance = squared_dist(vec2, vec1);
            if distance < d {
                d = distance;
                closest = (*vec1, *vec2);
            }
        }
    }
    return (d, closest);
}

fn trim_inp(s: &mut Vec<u8>) {
    while s.len() > 0 && s[s.len()-1] == b'\n' || s[s.len()-1] == b'\r' {
        s.pop();
    }
}

fn parse_inp(s: &[u8]) -> i64 {
    let mut res: i64 = 0;
    let mut decimal_idx = 0;
    for (i, c) in s.iter().rev().enumerate() {
        if *c == b'.' {
            decimal_idx = i;
            continue
        }
        if *c == b'-' {
            res = -res;
        } else if decimal_idx == 0 {
            res += (*c as i64 -48) * 10_i64.pow(i as u32) as i64;
        } else {
            res += (*c as i64 - 48) * 10_i64.pow((i-1) as u32) as i64;
        }
    }
    let offset = 2-decimal_idx;
    res *= 10_i64.pow(offset as u32);
    return res
}




fn brute_force(points: &[Point]) -> (i64, (Point, Point)) {
    let mut d = i64::MAX;
    let mut closest_pair = (Point{x: 0, y: 0}, Point{x: 0, y: 0});
    for i in 0..points.len()-1 {
        for j in (i+1)..(i+2).min(points.len()) {
            let vec1 = &points[i];
            let vec2 = &points[j];
            let distance = squared_dist(vec1, vec2);
            if distance < d {
                d = distance;
                closest_pair = (*vec1, *vec2);
            }
        }
    }
    return (d, closest_pair);
}

fn squared_dist(vec1: &Point, vec2: &Point) -> i64 {
    return (vec1.x-vec2.x).pow(2) + (vec1.y-vec2.y).pow(2);
}