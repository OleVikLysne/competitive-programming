use std::io;
use std::collections::{HashSet, VecDeque};
use std::cmp;
struct State {
    string: [u8; 8],
    clicks: u8,
}

fn rotate(l: &mut u8)  {
    *l = (*l+1) % 6;
}
fn main() {
    let mut a = String::with_capacity(10);
    let mut b = String::with_capacity(10);
    let _ = io::stdin().read_line(&mut a);
    let _ = io::stdin().read_line(&mut b);
    if a == b {
        println!("0");
        return
    }
    let mut start: [u8; 8] = [0; 8];
    for (i, e) in a[0..8].chars().map(|x| (x as u8)-65).enumerate() {
        start[i] = e;
    }
    let mut target: [u8; 8] = [0; 8];
    for (i, e) in b[0..8].chars().map(|x| (x as u8)-65).enumerate() {
        target[i] = e;
    }
    let mut visited = HashSet::new();
    let mut q = VecDeque::new();
    q.push_back(State{string: start, clicks: 0});
    visited.insert(start);
    
    loop {
        let state = q.pop_front().unwrap();
        for (i, icon) in state.string.into_iter().enumerate() {
            let mut temp_str = state.string;
            match icon {
                // A
                0 => { 
                    if i > 0 {
                        rotate(&mut temp_str[i-1]);
                    }
                    if i < 7 {
                        rotate(&mut temp_str[i+1]);
                    }
                },
                // B
                1 => { 
                    if i == 0 || i == 7 {continue}
                    temp_str[i+1] = temp_str[i-1];
                },
                // C
                2 => rotate(&mut temp_str[7-i]),
                // D
                3 => {
                    if i <= 3 {
                        for j in 0..i {
                            rotate(&mut temp_str[j])
                        }
                    }
                    else {
                        for j in i+1..8 {
                            rotate(&mut temp_str[j])
                        }
                    }
                },
                // E
                4 => {
                    if i == 0 || i == 7 {continue}
                    let y = cmp::min(i, 7-i);
                    rotate(&mut temp_str[i-y]);
                    rotate(&mut temp_str[i+y])
                },
                // F
                _ => {
                    let idx: usize;
                    if (i+1) % 2 != 0   {idx = (i+8)/2}
                    else                {idx = (i-1)/2}
                    rotate(&mut temp_str[idx])
                },
            }
            
            if temp_str == target {
                println!("{}", state.clicks+1);
                return
            }
            if visited.insert(temp_str) {
                q.push_back(State{string: temp_str, clicks: state.clicks+1})
            }
        }
    }
}