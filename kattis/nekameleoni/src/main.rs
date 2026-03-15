use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};


const INF: i32 = i32::MAX;
const NEG_INF: i32 = i32::MIN;
const K: usize = 50;
const N: usize = 100_000;

#[derive(Clone)]
struct Node {
    res: i32,
    leftmost: [i32; K],
    rightmost: [i32; K]
}

impl Node {
    fn new() -> Self {
        return Node{res: INF, leftmost: [INF; K], rightmost: [NEG_INF; K]}
    }

    fn calc_res(&mut self, l: &Node, r: &Node, k: &usize, arr: &[usize]) {
        self.res = l.res.min(r.res);
        let mut lis = [INF; K*2];
        let mut idx = 0;
        for i in 0..*k {
            if l.rightmost[i] == NEG_INF && r.leftmost[i] == INF {
                return
            }

            if l.rightmost[i] != NEG_INF {
                lis[idx] = l.rightmost[i];
                idx += 1;
            }
            if r.leftmost[i] != INF {
                lis[idx] = r.leftmost[i];
                idx += 1;
            }
        }

        lis[..idx].sort_unstable();
        let mut count = [0; K];
        let mut missing = *k;
        let mut j = 0;
        for i in &lis[..idx] {
            if count[arr[*i as usize]] == 0 {
                missing -= 1;
            }
            count[arr[*i as usize]] += 1;
            while count[arr[lis[j] as usize]] > 1 {
                count[arr[lis[j] as usize]] -= 1;
                j += 1;
            }
            if missing == 0 {
                self.res = self.res.min(i - lis[j] + 1);
            }

        }
    }

    fn merge(&mut self, l: &Node, r: &Node, k: &usize, arr: &[usize]) {
        self.calc_res(l, r, k, arr);
        for i in 0..K {
            self.leftmost[i] = l.leftmost[i].min(r.leftmost[i]);
            self.rightmost[i] = l.rightmost[i].max(r.rightmost[i]);
        }
    }
}

fn update(mut i: usize, v: usize, arr: &mut [usize], nodes: &mut [Node; N*2], k: &usize) {
    let prev = arr[i];
    arr[i] = v;
    nodes[i+N].leftmost[prev] = INF;
    nodes[i+N].rightmost[prev] = NEG_INF;
    nodes[i+N].leftmost[v] = i as i32;
    nodes[i+N].rightmost[v] = i as i32;
    i += N;
    while i > 1 {
        i >>= 1;
        let (l, r) = nodes.split_at_mut(2*i);
        l[i].merge(&r[0], &r[1], k, arr);
    }
}



fn main() {
    let mut io = IO::new();
    let mut nodes: [Node; N*2] = std::array::from_fn(|_| Node::new());
    let mut arr = [0; N];
    
    let (_, k, m): (u32, usize, u32) = io.r3();

    for (i, mut v) in io.line().enumerate() {
        v -= 1;
        arr[i] = v;
        nodes[i+N].leftmost[v] = i as i32;
        nodes[i+N].rightmost[v] = i as i32;
    }
    for i in (1..N).rev() {
        let (l, r) = nodes.split_at_mut(2*i);
        l[i].merge(&r[0], &r[1], &k, &arr);
    }
    
    for _ in 0..m {
        let mut iter = io.line();
        let qt: usize = iter.next().unwrap();
        if qt == 2 {
            if nodes[1].res != INF {
                print!("{} ", nodes[1].res);
            } else {
                print!("-1 ");
            }
        } else {
            let i = (iter.next().unwrap()) - 1;
            let v = (iter.next().unwrap()) - 1;
            update(i, v, &mut arr, &mut nodes, &k);
        }
    }

}

struct IO {
    buf: String,
    stdin: std::io::Stdin,
}

#[allow(dead_code)]
impl IO {
    fn new() -> Self {
        IO {
            buf: String::new(),
            stdin: std::io::stdin(),
        }
    }

    fn _rl(&mut self) {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
    }

    fn parse<T: FromStr>(&self, s: &str) -> T {
        unsafe { s.parse().unwrap_unchecked() }
    }

    fn parse_next<T: FromStr>(&self, line_split: &mut SplitAsciiWhitespace) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
    }

    fn line<T: FromStr>(&mut self) -> impl Iterator<Item = T> + '_ {
        self._rl();
        return self.buf.split_ascii_whitespace().map(|x| self.parse(x));
    }

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }
    
    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
    }

    fn chars(&mut self) -> Chars {
        self._rl();
        return self.buf.trim().chars();
    }

    fn all(&mut self) -> String {
        self.buf.clear();
        let _ = self.stdin.read_to_string(&mut self.buf);
        return self.buf.trim().to_string();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }

    fn r<T: FromStr>(&mut self) -> T {
        self._rl();
        self.parse(self.buf.trim())
    }

    fn r2<T1, T2>(&mut self) -> (T1, T2)
    where
        T1: FromStr,
        T2: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r4<T1, T2, T3, T4>(&mut self) -> (T1, T2, T3, T4)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r5<T1, T2, T3, T4, T5>(&mut self) -> (T1, T2, T3, T4, T5)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
        T5: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }
}
