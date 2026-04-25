#ifndef LINEALG_HPP
#define LINEALG_HPP

#include <array>

template<typename dataType, std::size_t N>
std::array<std::array<dataType, N>, N> eye()
{
    std::array<std::array<dataType, N>, N> matrix = {}; 
    
    for (std::size_t i = 0; i < N; ++i) {
        matrix[i][i] = 1;
    }
    return matrix;
}

template<typename dataType, std::size_t R1, std::size_t C1, std::size_t C2>
std::array<std::array<dataType, C2>, R1> multiplyMatrix(
    const std::array<std::array<dataType, C1>, R1>& A, 
    const std::array<std::array<dataType, C2>, C1>& B)
{
    std::array<std::array<dataType, C2>, R1> C = {};
    
    for (std::size_t i = 0; i < R1; ++i) {
        for (std::size_t j = 0; j < C2; ++j) {
            for (std::size_t k = 0; k < C1; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return C;
}

#endif