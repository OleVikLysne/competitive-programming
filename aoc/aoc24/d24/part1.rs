use std::collections::HashMap;

fn or(a: u32, b: u32) -> u32 {
    a | b
}
fn xor(a: u32, b: u32) -> u32 {
    a ^ b
}
fn and(a: u32, b: u32) -> u32 {
    a & b
}

fn get_op(str: &str) -> fn(u32, u32) -> u32 {
    return match str {
        "OR" => or,
        "XOR" => xor, 
        "AND" => and,
        _ => panic!()
    }
}



fn main() {
    let mut g: HashMap<String, Vec<String>> = HashMap::new();
    let mut stack = Vec::new();
    let mut values = HashMap::new();
    let mut ops = HashMap::new();
    let mut parents = HashMap::new();
    let mut visited: HashMap<String, u32> = HashMap::new();

    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        if line.trim() == "" {break}
        let (node, val) = line.split_once(" ").unwrap();
        let val = val.parse::<u32>().unwrap();
        let node = node.trim_end_matches(":").to_string();
        values.insert(node.clone(), val);
        stack.push(node);
    }

    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let mut iter = line.split_ascii_whitespace();
        let a = iter.next().unwrap().to_string();
        let op = get_op(iter.next().unwrap());
        let b = iter.next().unwrap().to_string();
        let _ = iter.next().unwrap();
        let c = iter.next().unwrap().to_string();
        g.entry(a.clone()).or_default().push(c.clone());
        g.entry(b.clone()).or_default().push(c.clone());
        ops.insert(c.clone(), op);
        parents.insert(c, (a, b));
    }

    println!("{:?}", g);

    while let Some(v) = stack.pop() {
        println!("{}", v);
        if let Some(children) = g.get(&v) {
            for u in children {
                let val = visited.entry(u.clone()).or_default();
                *val += 1;
                if *val == 2 {
                    let op = ops.get(u).unwrap();
                    let (p1, p2) = parents.get(u).unwrap();
                    let val1 = values.get(p1).unwrap();
                    let val2 = values.get(p2).unwrap();
                    values.insert(u.clone(), op(*val1, *val2));
                    stack.push(u.clone());
                }
            }
        }
    }
    let mut vector: Vec<(&String, &u32)> = values.iter().filter(|(key, val)| key.starts_with("z")).collect();
    vector.sort();
    vector.reverse();
    let value: String = vector.iter().map(|x| x.1.to_string()).collect();
    let value = u64::from_str_radix(&value, 2).unwrap();
    println!("{}", value);
}