fn get_reg(c: char) -> usize {
    let mut buf = String::new();
    let _ = std::io::stdin().read_line(&mut buf);
    let inp = buf.trim_start_matches(&format!("Register {}: ", c)).trim();
    return inp.parse().unwrap()
}

fn get_val(regs: &[usize], operand: usize) -> usize {
    if operand <= 3 {
        return operand
    }
    return regs[operand - 4]
}

fn adv(regs: &mut [usize], val: usize, pointer: &mut usize) {
    let val = get_val(regs, val);
    regs[0] /= 1 << val;
    *pointer += 2;
}

fn bxl(regs: &mut [usize], val: usize, pointer: &mut usize) {
    regs[1] ^= val;
    *pointer += 2;
}

fn bst(regs: &mut [usize], val: usize, pointer: &mut usize) {
    let val = get_val(regs, val);
    regs[1] = val % 8;
    *pointer += 2;
}

fn jnz(regs: &mut [usize], val: usize, pointer: &mut usize) {
    if regs[0] == 0 {
        *pointer += 2
    } else {
        *pointer = val
    }
}

fn bxc(regs: &mut [usize], _: usize, pointer: &mut usize) {
    regs[1] = regs[1] ^ regs[2];
    *pointer += 2;
}

fn out(regs: &mut [usize], val: usize, pointer: &mut usize) -> usize {
    let val = get_val(regs, val);
    *pointer += 2;
    return val % 8
}

fn bdv(regs: &mut [usize], val: usize, pointer: &mut usize) {
    let val = get_val(regs, val);
    regs[1] = regs[0] / (1 << val);
    *pointer += 2;
}

fn cdv(regs: &mut [usize], val: usize, pointer: &mut usize) {
    let val = get_val(regs, val);
    regs[2] = regs[0] / (1 << val);
    *pointer += 2;
}

fn run(program: &[usize], regs: &Vec<usize>, a_val: usize) -> Vec<usize> {
    let mut regs = regs.clone();
    regs[0] = a_val;
    let mut pointer = 0;
    let mut res = Vec::new();
    while pointer < program.len() {
        let (opcode, val) = (program[pointer], program[pointer+1]);
        if opcode == 0 {
            adv(&mut regs, val, &mut pointer);
        }
        else if opcode == 1 {
            bxl(&mut regs, val, &mut pointer);
        }
        else if opcode == 2 {
            bst(&mut regs, val, &mut pointer);
        }
        else if opcode == 3 {
            jnz(&mut regs, val, &mut pointer);
        }
        else if opcode == 4 {
            bxc(&mut regs, val, &mut pointer);
        }
        else if opcode == 5 {
            res.push(out(&mut regs, val, &mut pointer));
        }
        else if opcode == 6 {
            bdv(&mut regs, val, &mut pointer);
        }
        else if opcode == 7 {
            cdv(&mut regs, val, &mut pointer);
        }
    }
    return res
}


fn search(program: &[usize], regs: &Vec<usize>, mut i: usize, mut total: usize) -> usize {
    if i == 0 {
        return total;
    }
    i -= 1;
    let step = 2_usize.pow(3).pow(i as u32);
    loop {
        let res = run(&program, &regs, total);
        if res[i] == program[i] {
            let temp = search(program, regs, i, total);
            let res = run(&program, &regs, temp);
            if res[i] == program[i] {
                return temp
            }
        }
        total += step;
    }
}

fn main() {
    let stdin = std::io::stdin();
    let regs = vec![get_reg('A'), get_reg('B'), get_reg('C')];
    let mut buf = String::new();
    let _ = stdin.read_line(&mut String::new());
    let _ = stdin.read_line(&mut buf);
    let program: Vec<usize> = buf.trim_start_matches("Program: ").trim().split(",").map(|x| x.parse::<usize>().unwrap()).collect();
    let lower: usize = 1 << ((program.len() - 1)*3);
    println!("{}", lower);
    println!("{:?}", program);
    let foo = search(&program, &regs, program.len(), lower);
    println!("{:?}", run(&program, &regs, foo));
    println!("{}", foo)
}