use std::collections::HashMap;
fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let mut line = buf.split_whitespace().map(|x| x.parse::<u8>().unwrap());
    let w = line.next().unwrap();
    let h = line.next().unwrap();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let keys: Vec<u8> = buf.trim().chars().map(|x| x.to_digit(10).unwrap() as u8).collect();

    let mut grid: Vec<Vec<u8>> = Vec::new();
    let mut mem: HashMap<(u8, u8, u8), u16> = HashMap::new();
    for _ in 0..h {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        grid.push(buf.trim().chars().map(|d| d.to_digit(10).unwrap() as u8).collect());
    }
    println!("{}", foo(&mut mem, &grid, &keys, &w, 0, h-1, 0))

}

fn foo(
    mem: &mut HashMap<(u8, u8, u8), u16>, 
    grid: &Vec<Vec<u8>>, 
    keys: &Vec<u8>,
    w: &u8,
    x: u8, 
    y: u8, 
    k: u8
    ) -> u16 {
    if mem.contains_key(&(x,y,k)) {
        return mem[&(x,y,k)]
    }
    if x == w-1 && y==0 {
        let ret = grid[y as usize][x as usize] as u16;
        mem.insert((x,y,k), ret);
        return ret;
    }
    let val = grid[y as usize][x as usize] as u16;
    let ret: u16;
    let mut right = u16::MAX;
    let mut up = u16::MAX;
    if x+1 < *w {
        right = foo(mem, grid, keys, w, x+1, y, k);
    }
    if y as i8 -1 >= 0 {
        up = foo(mem, grid, keys, w, x, y-1, k);
    }
    if (k as usize) < keys.len() {
        let mut right_hop = u16::MAX;
        let mut up_hop = u16::MAX;
        if x + keys[k as usize]+1 < *w {
            right_hop = foo(mem, grid, keys, w, x+keys[k as usize]+1, y, k+1);
        }
        if (y as i8) - (keys[k as usize]) as i8 > 0 {
            up_hop = foo(mem, grid, keys, w, x, y-keys[k as usize]-1, k+1);
        }
        ret = val + right.min(right_hop).min(up).min(up_hop);
    }
    else {
        ret = val+right.min(up);
    }
    mem.insert((x,y,k), ret);
    return ret;
}