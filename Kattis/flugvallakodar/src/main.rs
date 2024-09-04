use std::io::BufRead;

const PRIMES: [u128; 26] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];

struct Node {
    mask: u128,
    children: [Option<Box<Node>>; 26]
}

impl Node {
    fn new() -> Node {
        Node{
            mask: 1,
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
        let mut mask: u128 = 1;
        name.truncate(name.trim_ascii_end().len());
        for c in name.iter_mut() {
            *c -= 65;
            if *c > 26 {
                *c -= 32
            }
            if mask % PRIMES[*c as usize] != 0 {
                mask *= PRIMES[*c as usize];
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
    mask: &mut u128, 
    char_occ: &mut [u16]
) -> Option<[u8; 3]> {

    if depth == 2 {
        if node.mask % *mask == 0 {
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
            *mask /= PRIMES[char]
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
                        node.mask *= PRIMES[char];
                        arr[depth as usize] = name[j];
                        return Some(arr)
                    }
                }
            }
        }
    }
    None
}