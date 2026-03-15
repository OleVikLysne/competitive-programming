use std::cmp::Ordering;

#[derive(Copy, Clone)]
struct Vector {
    x: i32,
    y: i32,
}

fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let mut points = [Vector{x: 0, y: 0}; 100000];

    let _ = stdin.read_line(&mut buf);
    let trimmed_buf = buf.trim();
    let c: usize = trimmed_buf.parse().unwrap();
    buf.clear();
    for i in 0..c {
        let _ = stdin.read_line(&mut buf);
        let mut coords_iter = buf.split_ascii_whitespace();
        let x: i32 = coords_iter.next().unwrap().parse().unwrap();
        let y: i32 = coords_iter.next().unwrap().parse().unwrap();
        points[i] = Vector{x, y};
        buf.clear();
    }
    let hull = graham_scan(&mut points[..c]);
    println!("{}", rotating_calipers(&hull));
}

fn graham_scan(points: &mut [Vector]) -> Vec<Vector> {
    let mut anchor_index = 0;
    let anchor = 
        {
            let mut anchor = &points[0];
            for (i, point) in points[1..].iter().enumerate() {
                if point.y < anchor.y || (point.y == anchor.y && point.x < anchor.x) {
                    anchor = point;
                    anchor_index = i+1;
                }
            }
            *anchor
        };
    points.swap(anchor_index, 0);
    points[1..].sort_unstable_by(|v1, v2| compare(&anchor, v1, v2));
    let mut hull = vec![anchor];
    for point in &points[1..] {
        while hull.len() > 1 && orient(&hull[hull.len()-2], &hull[hull.len()-1], point) >= 0 {
            hull.pop();
        }
        hull.push(*point);
    }
    return hull
}

fn rotating_calipers(hull: &Vec<Vector>) -> f32 {
    let n = hull.len();
    let mut max_distance = 0;
    for i in 0..n {
        let mut j = (i+1) % n;
        let mut k  = (j+1) % n;
        while squared_dist(&hull[i], &hull[j]) < squared_dist(&hull[i], &hull[k]) {
            j = k;
            k = (k+1) % n;
        }
        max_distance = max_distance.max(squared_dist(&hull[i], &hull[j]));
    }

    return (max_distance as f32).sqrt()
}

fn squared_dist(v1: &Vector, v2: &Vector) -> i32 {
    return (v1.x-v2.x).pow(2)+(v1.y-v2.y).pow(2)
}

fn cross(v1: &Vector, v2: &Vector) -> i32 {
    return v1.x*v2.y - v2.x*v1.y
}

fn orient(anchor: &Vector, v1: &Vector, v2: &Vector) -> i32 {
    let foo = Vector{x: v1.x-anchor.x, y: v1.y-anchor.y};
    let bar = Vector{x: v2.x-anchor.x, y: v2.y-anchor.y};
    return cross(&foo, &bar)
}

fn compare(anchor: &Vector, v1: &Vector, v2: &Vector) -> Ordering {
    let o = orient(anchor, v1, v2);
    if o >= 0 {
        return Ordering::Greater
    }
    return Ordering::Less
}