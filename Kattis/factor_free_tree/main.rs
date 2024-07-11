const MAX_NODES: usize = 1_000_000;
const MAX_VAL: usize = 10_000_000;

fn main() {
    let mut parent: [i32; MAX_NODES] = [-1; MAX_NODES];
    let primes = sieve();
    let mut factor_to_nodes: Vec<Vec<i32>> = vec![Vec::new(); MAX_NODES];
    let mut node_to_factors: Vec<Vec<i32>> = Vec::new();

    let stdin = std::io::stdin();
    let mut buf = String::new();

    let _ = stdin.read_line(&mut buf);
    let n: i32 = buf.trim().parse().unwrap();
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    for (i, x) in buf.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).enumerate() {
        let factors = factorize(x, &primes);
        for fact in factors.iter() {
            factor_to_nodes[*fact as usize].push(i as i32);
        }
        node_to_factors.push(factors);
    }
    let bounds = compute_bounds(&node_to_factors, &factor_to_nodes);

    if search(0, n-1, -1, &mut parent, &bounds) {
        parent[0..n as usize].iter().for_each(|x| print!("{} ", x+1))
    } else {
        print!("impossible")
    }
}


fn search(l: i32, r: i32, prev: i32, parent: &mut [i32], bounds: &[(i32, i32)]) -> bool {
    if l >= r {
        if l == r {
            parent[l as usize] = prev;
        }
        return true
    }
    for mut i in 0..=r-l {
        if i % 2 == 0 {
            i = l+(i/2)
        } else {
            i = r-(i/2)
        }
        let lb = bounds[i as usize].0;
        let rb = bounds[i as usize].1;
        if lb < l && rb > r {
            parent[i as usize] = prev;
            return search(l, i-1, i, parent, bounds) && search(i+1, r, i, parent, bounds)
        }
    }
    return false
}

fn compute_bounds(node_to_factors: &Vec<Vec<i32>>, factor_to_nodes: &Vec<Vec<i32>>) -> Vec<(i32, i32)> {
    let mut bounds = Vec::new();
    let n = node_to_factors.len() as i32;
    for (i, factors) in node_to_factors.iter().enumerate().map(|(x, y)| (x as i32, y)) {
        let mut lb: i32 = -1;
        let mut rb: i32 = n;
        for fact in factors {
            let l = &factor_to_nodes[*fact as usize];
            
            let idx = l.binary_search(&(i)).unwrap();
            if idx > 0 {
                lb = lb.max(l[idx-1])
            }
            if idx < l.len()-1 {
                rb = rb.min(l[idx+1])
            }
        }
        bounds.push((lb, rb));
    }
    return bounds
}

fn factorize(mut n: i32, primes: &[i32]) -> Vec<i32> {
    let mut factors: Vec<i32> = Vec::new();
    for (i, p) in primes.iter().enumerate().map(|(i, p)| (i as i32, p)) {
        if p*p > n { break }
        if n % p == 0 {
            factors.push(i);
            while n % p == 0 {
                n /= p;
            }
        }
    }
    if n > 1 {
        factors.push(primes.binary_search(&n).unwrap() as i32);
    }
    return factors
}


fn sieve() -> Vec<i32> {
    let mut prime: [bool; MAX_VAL] = [true; MAX_VAL];
    let mut l = Vec::new();
    prime[0] = false;
    prime[1] = false;
    for i in 2..MAX_VAL {
        if !prime[i] {
            continue
        }
        l.push(i as i32);
        for j in (i*2..MAX_VAL).step_by(i) {
            prime[j] = false;
        }
    }
    return l
}