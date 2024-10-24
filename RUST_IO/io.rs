use std::fmt::Display;

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

    fn parse<T: std::str::FromStr>(&self, s: &str) -> T {
        unsafe { s.parse::<T>().unwrap_unchecked() }
    }

    fn parse_next<T: std::str::FromStr>(&self, foo: &mut std::str::SplitAsciiWhitespace) -> T {
        unsafe { self.parse(foo.next().unwrap_unchecked()) }
    }

    fn r<T: std::str::FromStr>(&mut self) -> T {
        let _ = self.stdin.read_line(&mut self.buf);
        let res = self.parse(self.buf.trim());
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
        let a = self.parse_next(&mut foo);
        let b = self.parse_next(&mut foo);
        self.buf.clear();
        (a, b)
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
    {
        let _ = self.stdin.read_line(&mut self.buf);
        let mut foo = self.buf.split_ascii_whitespace();
        let a = self.parse_next(&mut foo);
        let b = self.parse_next(&mut foo);
        let c = self.parse_next(&mut foo);
        self.buf.clear();
        (a, b, c)
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
        let a = self.parse_next(&mut foo);
        let b = self.parse_next(&mut foo);
        let c = self.parse_next(&mut foo);
        let d = self.parse_next(&mut foo);
        self.buf.clear();
        (a, b, c, d)
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
        let a = self.parse_next(&mut foo);
        let b = self.parse_next(&mut foo);
        let c = self.parse_next(&mut foo);
        let d = self.parse_next(&mut foo);
        let e = self.parse_next(&mut foo);
        self.buf.clear();
        (a, b, c, d, e)
    }

    fn vec<T: std::str::FromStr>(&mut self) -> Vec<T> {
        let _ = self.stdin.read_line(&mut self.buf);
        let res = self
            .buf
            .split_ascii_whitespace()
            .map(|x| self.parse(x))
            .collect();
        self.buf.clear();
        res
    }

    fn print_vec<T: Display>(&self, vec: &Vec<T>) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}

fn main() {
    let mut io = IO::new();
}
