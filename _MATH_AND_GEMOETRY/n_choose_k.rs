const PASC_SIZE: usize = 31;
fn pascals_triangle() -> [[u32; PASC_SIZE]; PASC_SIZE] {
    let mut triangle = [[1; PASC_SIZE]; PASC_SIZE];
    for i in 1..PASC_SIZE {
        for j in 1..i {
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1];
        }
    }
    return triangle
}