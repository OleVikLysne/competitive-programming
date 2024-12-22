const MOD: u64 = 16777216;
const STEPS: u32 = 2000;

fn evolve(mut bit_string: u64) -> u64 {
    for _ in 0..STEPS {
        bit_string ^= bit_string * 64;
        bit_string %= MOD;
        
        bit_string ^= bit_string / 32;
        bit_string %= MOD;
        
        bit_string ^= bit_string * 2048;
        bit_string %= MOD;
    }
    bit_string
}

fn main() {
    let mut total = 0;
    for line in std::io::stdin().lines().map(|x| x.unwrap()) {
        let bit_string = line.parse().unwrap();
        total += evolve(bit_string);
    }
    println!("{}", total)

}