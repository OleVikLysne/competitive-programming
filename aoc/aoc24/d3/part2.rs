use regex::Regex;

fn main() {
    let stdin = std::io::stdin();
    let re = Regex::new(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|do\(\)|don't\(\)").unwrap();
    let mut s = 0;
    let mut include = true;

    for line in stdin.lines().map(|x| x.unwrap()) {
        for m in re.find_iter(&line).map(|x| x.as_str()) {
            if m == "do()" {
                include = true;
                continue
            } else if m == "don't()" {
                include = false;
                continue
            }
            if !include  {
                continue
            }
            let a = m
                .strip_prefix("mul")
                .unwrap()
                .trim_matches(|c| c == '(' || c == ')');
            let mut foo = a.split(',');
            let x = foo.next().unwrap().parse::<i32>().unwrap();
            let y = foo.next().unwrap().parse::<i32>().unwrap();
            s += x * y;
        }
    }
    println!("{}", s);
}
