use std::fmt::Display;

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

    fn print_vec<T>(&self, vec: &Vec<T>) 
        where 
        T: Display
    {
        for x in vec {
            print!("{} ", *x);
        }
    }
}


fn main() {
    let mut io = IO::new();
}
