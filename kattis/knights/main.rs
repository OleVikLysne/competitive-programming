use std::collections::{HashMap, HashSet, VecDeque};
fn main() {
    let moves: [[i8; 2]; 8] = [ [1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2, 1], [-2,-1] ];
    let target_board: [[i8; 5]; 5] = [
        [1,1,1,1,1],
        [0,1,1,1,1],
        [0,0,-1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,0]
    ];
    let mut target = HashMap::new();
    let mut q = VecDeque::new();
    q.push_back((target_board, 2, 2, 0));
    while let Some(v) = q.pop_front() {
        let mut board = v.0;
        let k: u8 = v.3;
        target.insert(board, k);
        if k+1 > 5 { continue }
        let i = v.1;
        let j = v.2;
        for a in moves.iter().map(|a| [i+a[0], j+a[1]]).filter(|a| a[0]<5 && a[0]>=0 && a[1]<5 && a[1]>=0) {
            let x = a[0] as usize;
            let y = a[1] as usize;
            let i = i as usize;
            let j = j as usize;
            board[i][j] = board[x][y];
            board[x][y] = -1;
            if !target.contains_key(&board) {
                q.push_back((board, a[0], a[1], k+1));
            }
            board[x][y] = board[i][j];
            board[i][j] = -1;
        }
    }

    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let n: u8 = buf.trim().parse().unwrap();
    let mut visited = HashSet::new();
    buf.clear();
    for _ in 0..n {
        let mut start_pos: (i8, i8) = (-1, -1);
        let mut board = [[0; 5]; 5];
        for i in 0..5 {
            let _ = stdin.read_line(&mut buf);
            for (j, x) in buf[0..5].chars().enumerate() {
                if x == ' ' {
                    start_pos.0 = i;
                    start_pos.1 = j as i8;
                    board[i as usize][j] = -1;
                }
                else {
                    board[i as usize][j] = x.to_digit(10).unwrap() as i8;
                }
            }
        buf.clear();
        }

        let mut dummy = true;
        q.push_back((board, start_pos.0, start_pos.1, 0));
        while let Some(v) = q.pop_front() {
            let mut board = v.0;
            let i = v.1;
            let j = v.2;
            let k: u8 = v.3;
            if let Some(u) = target.get(&board) { 
                println!("Solvable in {} move(s).", *u+k);
                dummy = false;
                break
            }
            if k+1 > 5 || !visited.insert(board) { continue }
            for a in moves.iter().map(|a| [i+a[0], j+a[1]]).filter(|b| b[0]<5 && b[0]>=0 && b[1]<5 && b[1]>=0) {
                let x = a[0] as usize;
                let y = a[1] as usize;
                let i = i as usize;
                let j = j as usize;
                board[i][j] = board[x][y];
                board[x][y] = -1;
                q.push_back((board, a[0], a[1], k+1));
                board[x][y] = board[i][j];
                board[i][j] = -1;
            }
        }
        if dummy {
            println!("Unsolvable in less than 11 move(s).");
        }
        q.clear();
        visited.clear();
    }
}