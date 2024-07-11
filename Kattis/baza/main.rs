use std::collections::HashMap;
use std::io::BufRead;


struct Node {
    count: u32,
    children: [Option<Box<Node>>; 26],
}

impl Node {
    fn new() -> Node {
        Node{
            count: 0, 
            children: 
            [
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
            ],
        }
    }
}

fn main() {
    let mut root = Node::new();
    let mut words: HashMap<Vec<u8>, u32> = HashMap::new();
    let stdin = std::io::stdin();
    let mut handle = stdin.lock();
    
    let mut buf = String::new();
    let _ = handle.read_line(&mut buf);
    let n: u32 = buf.trim().parse().unwrap();
    buf.clear();

    let mut word = Vec::new();
    for _ in 0..n {
        word.clear();
        let _ = handle.read_until(b'\n', &mut word);
        word.pop();
        let s = add(&mut root, &word);
        words.insert(word.clone(), s);
    }
    let _ = handle.read_line(&mut buf);
    let q: u32 = buf.trim().parse().unwrap();

    for _ in 0..q {
        word.clear();
        let _ = handle.read_until(b'\n', &mut word);
        word.pop();

        let s = {
            if let Some(v) = words.get(&word) {
                *v
            } else {
                find(&root, &word)
            }
        };
        println!("{}", s);
    }
}

fn add(root: &mut Node, word: &[u8]) -> u32 {
    root.count += 1;
    let mut s = root.count;
    let mut current = root;
    for char in word.iter().map(|x| *x as usize-97) {
        current = {
            if current.children[char].is_some() {
                current.children[char].as_mut().unwrap()
            } else {
                current.children[char] = Some(Box::new(Node::new()));
                current.children[char].as_mut().unwrap()
            }
        };
        current.count += 1;
        s += current.count;
    }
    return s
}

fn find(root: &Node, word: &[u8]) -> u32 {
    let mut s = root.count;
    let mut current = root;

    for char in word.iter().map(|x| *x as usize-97) {
        current = match current.children[char].as_ref() {
            None => return s,
            Some(v) => v
        };
        s += current.count;
    }
    return s
}