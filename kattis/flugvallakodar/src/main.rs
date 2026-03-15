use std::io::BufRead;

struct Node {
    mask: u32,
    children: [Option<Box<Node>>; 26]
}

impl Node {
    fn new() -> Node {
        Node{
            mask: 0,
            children: Default::default()
        }
    }
}

fn main() -> Result<(), std::num::ParseIntError>{
    let stdin = std::io::stdin();
    let mut handle = stdin.lock();
    let mut buf = String::new();
    let _ = handle.read_line(&mut buf);
    let n: u32 = buf.trim().parse()?;
    
    let mut root = Node::new();
    let mut name = Vec::new();
    for _ in 0..n {
        name.clear();
        let _ = handle.read_until(b'\n', &mut name);
        let mut char_occ: [u16; 26] = [0; 26];
        let mut mask: u32 = 0;
        name.truncate(name.trim_ascii_end().len());
        for c in name.iter_mut() {
            *c -= 65;
            if *c > 26 {
                *c -= 32
            }
            if mask & 1 << *c == 0 {
                mask |= 1 << *c
            }
            char_occ[*c as usize] += 1;
        }

        match search(0, &mut root, 0, &name, &mut mask, &mut char_occ) {
            None => print!(":( "),
            Some(arr) => {
                for c in arr.iter().map(|x| (*x+65) as char) {
                    print!("{}", c);
                }
                print!(" ");
            }
        }
    }
    Ok(())
}

fn search(
    i: usize,
    node: &mut Node,
    depth: u8,
    name: &[u8],
    mask: &mut u32, 
    char_occ: &mut [u16]
) -> Option<[u8; 3]> {

    if depth == 2 {
        if node.mask & *mask == *mask {
            return None
        }
    }
    if depth == 3 {
        return Some([u8::MAX; 3])
    }
    let mut visited = [false; 26];
    for j in i..name.len() {
        let char = name[j] as usize;
        char_occ[char] -= 1;
        if visited[char] {
            continue
        }
        visited[char] = true;
        if char_occ[char] == 0 {
            *mask ^= 1 << char;
        }
        match node.children[char].as_mut() {
            Some(next_node) => {
                if depth == 2 { continue }
                match search(j+1, next_node, depth+1, name, mask, char_occ) {
                    None => {},
                    Some(mut arr) => {
                        arr[depth as usize] = name[j];
                        return Some(arr)
                    }
                }
            },
            None => {
                node.children[char] = Some(Box::new(Node::new()));
                let next_node = node.children[char].as_mut()?;
                match search(j+1, next_node, depth+1, name, mask, char_occ) {
                    None => {},
                    Some(mut arr) => {
                        node.mask |= 1 << char;
                        arr[depth as usize] = name[j];
                        return Some(arr)
                    }
                }
            }
        }
    }
    None
}