use std::collections::{BinaryHeap, HashMap};


fn main() {
    let mut total = 0;

    let lines: Vec<String> = std::io::stdin().lines().map(|x| x.unwrap()).collect();
    for i in (0..lines.len()).step_by(4) {
        let a = lines[i].trim_start_matches("Button A: ");
        let b = lines[i+1].trim_start_matches("Button B: ");
        let p = lines[i+2].trim_start_matches("Prize: ");

        let mut v: Vec<(i32, i32)> = Vec::new();
        for z in [a, b, p] {
            let mut foo = z.split_ascii_whitespace();
            let left = foo.next().unwrap().trim_start_matches("X").trim_start_matches("Y").trim_start_matches("=").trim_end_matches(",");
            let right = foo.next().unwrap().trim_start_matches("X").trim_start_matches("Y").trim_start_matches("=");
            println!("{} {}", left, right);
            v.push((left.parse().unwrap(), right.parse().unwrap()));
        }

        let (t_x, t_y) = v[2];
        let mut pq = BinaryHeap::new();
        pq.push((-3, v[0].0, v[0].1));
        pq.push((-1, v[1].0, v[1].1));

        let mut dist = HashMap::new();
        dist.insert(v[0], 3);
        dist.insert(v[1], 1);

        while let Some((d, x, y)) = pq.pop() {
            let d = -d;
            if *dist.get(&(x, y)).unwrap() > d {
                continue
            }
            if x == t_x && y == t_y {
                total += d;
                break
            }
            if x > t_x && y > t_y {continue}
            for (cost, dx, dy) in [(3, v[0].0, v[0].1), (1, v[1].0, v[1].1)] {
                let new_d = d + cost;
                let new_pos = (x+dx, y+dy);
                match dist.entry(new_pos) {
                    std::collections::hash_map::Entry::Occupied(mut occupied_entry) => {
                        let val = occupied_entry.get_mut();
                        if *val > new_d {
                            *val = new_d;
                            pq.push((-new_d, new_pos.0, new_pos.1))
                        }
                    },
                    std::collections::hash_map::Entry::Vacant(vacant_entry) => {
                        vacant_entry.insert(new_d);
                        pq.push((-new_d, new_pos.0, new_pos.1))
                    }
                }
            }
        }
    }
    println!("{}", total)
}