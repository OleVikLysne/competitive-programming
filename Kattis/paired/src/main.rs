use std::collections::HashMap;

fn main() -> Result<(), std::num::ParseIntError> {

    let mut arr: [i32; 100000] = [0; 10_usize.pow(5)];
    let mut occ: [i32; 100001] = [0; 10_usize.pow(5)+1];
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let _ = stdin.read_line(&mut buf);
    let n: usize = buf.trim().parse()?;
    buf.clear();
    let _ = stdin.read_line(&mut buf);

    let mut stack = Vec::new();
    let mut j = 0;
    for (i, x) in buf.split_whitespace().enumerate() {
        let x = x.parse()?;
        arr[i] = x;
        occ[x as usize] += 1;

        if occ[x as usize] == 3 {
            stack.push((j as u32, i as u32));
            while arr[j] != x {
                occ[arr[j] as usize] -= 1;
                j += 1
            }
            j += 1;
            occ[x as usize] -= 1;
        }
    }
    stack.push((j as u32, n as u32));

    let mut longest = 0;
    while let Some((j, n)) = stack.pop() {
        if (n-j) - ((n-j) % 2) <= longest {
            continue
        }
        let mut occ: HashMap<i32, i32> = HashMap::new();
        let mut once = 0;
        for i in j..n {
            let x = arr[i as usize];
            let count = occ.entry(x).or_insert(0);
            *count += 1;
            if *count == 1 {
                once += 1;
            } else if *count == 2 {
                once -= 1;
            }
        }

        if once == 0 {
            longest = longest.max((n-j) as u32);
            continue
        }

        let mut k = j;
        for i in j..n {
            if occ[&arr[i as usize]] == 1 {
                stack.push((k, i));
                k = i+1;
            }
        }
        stack.push((k, n));
    }
    println!("{}", longest);
    Ok(())
}
