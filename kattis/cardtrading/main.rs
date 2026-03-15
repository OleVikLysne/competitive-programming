use std::collections::HashMap;
#[allow(non_snake_case)]
fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut ntk = buf.split_whitespace().skip(1);
    let T = ntk.next().unwrap().parse::<usize>().unwrap();
    let K = ntk.next().unwrap().parse::<usize>().unwrap();
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    let A = buf.split_whitespace().map(|e| e.parse::<usize>().unwrap()-1);
    let mut A_cards = HashMap::new();
    for card in A {
        if A_cards.insert(card, 1) != None {
            A_cards.insert(card, 2);
        }
    }
    let mut sell: Vec<i64> = Vec::with_capacity(T);
    let mut profit = 0;
    for t in 0..T {
        buf.clear();
        let _ = stdin.read_line(&mut buf);
        let mut card_type = buf.split_whitespace().map(|e| e.parse::<i64>().unwrap());
        let a = card_type.next().unwrap();
        let b = card_type.next().unwrap();
        match A_cards.get(&t) {
            None => {
                sell.push(2*a);
                profit-=2*a;
            }
            Some(c) => {
                if c == &1 {
                    sell.push(a+b);
                    profit-=a;
                }
                else {
                    sell.push(2*b);
                }
            }
        }
    }

    sell.sort_unstable_by(|x,y| y.cmp(x));
    profit += &sell[0..(T-K)].into_iter().sum();
    println!("{}", profit);
}
