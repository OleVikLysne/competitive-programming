use std::collections::HashMap;
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut line = buf.split_whitespace();
    let n: u8 = line.next().unwrap().parse().unwrap();
    let k: u8 = line.next().unwrap().parse().unwrap();
    let mut grid: Vec<[u8; 2]> = Vec::with_capacity(n as usize);
    for _ in 0..n {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut line = buf.split_whitespace();
        let x: u8 = line.next().unwrap().parse().unwrap();
        let y: u8 = line.next().unwrap().parse().unwrap();
        grid.push([x, y]);
        //grid.push(buf.split_whitespace().map(|x| x.parse::<u8>().unwrap()).collect());
    }
    let mut mem: HashMap<(u8, u8, u8), i16> = HashMap::new();
    println!("{}", foo(&mut mem, &grid, &n, &k, 0, 0, (u8::MAX-1, u8::MAX-1)))
}

fn foo(
    mem: &mut HashMap<(u8, u8, u8), i16>, 
    grid: &Vec<[u8; 2]>,
    n: &u8,
    k: &u8,
    i: u8, 
    blocks: u8, 
    last_block: (u8, u8)
    ) -> i16 {
    let state;
    if last_block.0+1 < i || last_block.0 == u8::MAX-1 {state=2}
    else {state=last_block.1}
    if mem.contains_key(&(i, blocks, state)) {
        return mem[&(i, blocks, state)];
    }
    if blocks == *k {
        return grid[(i as usize)..].into_iter().flat_map(IntoIterator::into_iter).map(|x| *x as i16).sum::<i16>();
    }
    if n-i < k-blocks {
        return i16::MIN;
    }
    let val: i16;
    if last_block.0 + 1 == i{ 
        let v0 = grid[i as usize][((last_block.1+1)%2) as usize] as i16
                     +foo(mem, grid, n, k, i+1, blocks+1, (i, last_block.1));
        let v1 = (grid[i as usize][0]+grid[i as usize][1]) as i16
                      +foo(mem, grid, n, k, i+1, blocks, last_block);
        val = v0.max(v1);
        
    }
    else {
        let v0 = grid[i as usize][1] as i16 + foo(mem, grid, n, k, i+1, blocks+1, (i, 0));
        let v1 = grid[i as usize][0] as i16 + foo(mem, grid, n, k, i+1, blocks+1, (i, 1));
        let v2 = (grid[i as usize][0]+grid[i as usize][1]) as i16 + foo(mem, grid, n, k, i+1, blocks, last_block);
        val = v0.max(v1).max(v2);
    }
    mem.insert((i, blocks, state), val);
    return val;
}
