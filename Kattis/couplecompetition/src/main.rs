use std::collections::VecDeque;

struct IO {
    buf: String,
    stdin: std::io::Stdin,
}

#[allow(dead_code)]
impl IO {
    fn new() -> Self {
        let buf = String::new();
        let stdin = std::io::stdin();
        IO { buf, stdin }
    }

    fn r<T>(&mut self) -> T
    where
        T: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let res = unsafe {self.buf.trim().parse::<T>().unwrap_unchecked() };
        self.buf.clear();
        res
    }

    
    fn r2<T1, T2>(&mut self) -> (T1, T2)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let mut foo = self.buf.split_ascii_whitespace();
        unsafe {
            let a = foo.next().unwrap_unchecked().parse::<T1>().unwrap_unchecked();
            let b = foo.next().unwrap_unchecked().parse::<T2>().unwrap_unchecked();
            self.buf.clear();
            (a, b)
        }
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let mut foo = self.buf.split_ascii_whitespace();
        unsafe {
            let a = foo.next().unwrap_unchecked().parse::<T1>().unwrap_unchecked();
            let b = foo.next().unwrap_unchecked().parse::<T2>().unwrap_unchecked();
            let c = foo.next().unwrap_unchecked().parse::<T3>().unwrap_unchecked();
            self.buf.clear();
            (a, b, c)
        }
    }

    fn r4<T1, T2, T3, T4>(&mut self) -> (T1, T2, T3, T4)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
        T4: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let mut foo = self.buf.split_ascii_whitespace();
        unsafe {
            let a = foo.next().unwrap_unchecked().parse::<T1>().unwrap_unchecked();
            let b = foo.next().unwrap_unchecked().parse::<T2>().unwrap_unchecked();
            let c = foo.next().unwrap_unchecked().parse::<T3>().unwrap_unchecked();
            let d = foo.next().unwrap_unchecked().parse::<T4>().unwrap_unchecked();
            self.buf.clear();
            (a, b, c, d)
        }
    }

    fn r5<T1, T2, T3, T4, T5>(&mut self) -> (T1, T2, T3, T4, T5)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
        T4: std::str::FromStr,
        T5: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let mut foo = self.buf.split_ascii_whitespace();
        unsafe {
            let a = foo.next().unwrap_unchecked().parse::<T1>().unwrap_unchecked();
            let b = foo.next().unwrap_unchecked().parse::<T2>().unwrap_unchecked();
            let c = foo.next().unwrap_unchecked().parse::<T3>().unwrap_unchecked();
            let d = foo.next().unwrap_unchecked().parse::<T4>().unwrap_unchecked();
            let e = foo.next().unwrap_unchecked().parse::<T5>().unwrap_unchecked();
            self.buf.clear();
            (a, b, c, d, e)
        }
    }

    fn vec<T>(&mut self) -> Vec<T> 
        where
        T: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        unsafe {
            let res = self.buf.split_ascii_whitespace().map(|x| x.parse::<T>().unwrap_unchecked()).collect();
            self.buf.clear();
            res
        }
    }
}

fn main() -> Result<(), std::num::ParseIntError> {
    let mut io = IO::new();
    let n = io.r();
    let mut arr: Vec<u32> = Vec::new();
    for _ in 0..n {
        arr.push(io.r());
    }

    let mut start = vec![0];
    for i in 1..n {
        if arr[i] >= arr[start[0]] {
            if arr[i] > arr[start[0]] {
                start.clear();
            }
            start.push(i);
        } 
    }

    let mut res = vec![-1; n];
    let mut m = vec![vec![usize::MAX; 2]; n];
    for i in (0..n).rev() {
        for j in i+1..n {
            if arr[j] > arr[i] {
                m[i][0] = j;
                break
            }
            let k = m[j][0];
            if k == usize::MAX || arr[k] > arr[i] {
                m[i][0] = k;
                break
            }

        }
    }
    
    for i in 0..n {
        for j in (0..i).rev() {
            if arr[j] > arr[i] {
                m[i][1] = j;
                break
            }
            let k = m[j][1];
            if k == usize::MAX || arr[k] > arr[i] {
                m[i][1] = k;
                break
            }

        }
    }

    let mut rev_m = vec![Vec::new(); n];
    for i in 0..n {
        for j in &m[i] {
            if *j != usize::MAX {
                rev_m[*j].push(i);
            }
        }
    }
    let mut q = VecDeque::new();
    for i in start.iter() {
        res[*i] = 0;
        q.push_back((*i, 0))
    }
    while let Some((i, c)) = q.pop_front() {
        for j in rev_m[i].iter() {
            if res[*j] == -1 {
                res[*j] = c+1;
                q.push_back((*j, c+1));
            }
        }
    }
    for x in res {
        print!("{} ", x);
    }
    Ok(())
}
