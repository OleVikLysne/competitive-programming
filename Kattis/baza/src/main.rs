use std::{io::BufRead, num::ParseIntError};

struct Node {
    count: u32,
    children: [Option<Box<Node>>; 26],
    val: u32
}
impl Node {
    fn new() -> Node {
        Node{
            count: 0, 
            children: Default::default(),
            val: u32::MAX
        }
    }
}

fn main() -> Result<(), ParseIntError> {
    let mut root = Node::new();
    let stdin = std::io::stdin();
    let mut handle = stdin.lock();
    let mut buf = String::new();
    let _ = handle.read_line(&mut buf);
    let n: u32 = buf.trim().parse()?;
    buf.clear();

    let mut word = Vec::with_capacity(31);
    for _ in 0..n {
        word.clear();
        let _ = handle.read_until(b'\n', &mut word);
        word.pop();
        add(&mut root, &word);
    }
    let _ = handle.read_line(&mut buf);
    let q: u32 = buf.trim().parse()?;

    for _ in 0..q {
        word.clear();
        let _ = handle.read_until(b'\n', &mut word);
        word.pop();
        print!("{} ", find(&root, &word))
    }
    Ok(())
}

fn add(root: &mut Node, word: &[u8]) -> Option<()> {
    root.count += 1;
    let mut s = root.count;
    let mut current = root;
    for char in word.iter().map(|x| (*x-97) as usize) {
        if current.children[char].is_none() {
            current.children[char] = Some(Box::new(Node::new()))
        }
        current = current.children[char].as_mut()?;
        current.count += 1;
        s += current.count
    }
    current.val = s;
    Some(())
}

fn find(root: &Node, word: &[u8]) -> u32 {
    let mut s = root.count;
    let mut current = root;
    for char in word.iter().map(|x| (*x-97) as usize) {
        current = match current.children[char].as_ref() {
            Some(v) => v,
            None => return s
        };
        s += current.count
    }
    if current.val != u32::MAX {
        return current.val
    }
    return s
}