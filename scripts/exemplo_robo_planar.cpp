#include <iostream>
#include <vector>
#include <cmath>
#include <memory>
#include <iomanip>
#include "frame.hpp"
#include "junta.hpp"
#include "robo.hpp"

using namespace std;

int main() {
    // =======================================================
    // 1. CONFIGURAÇÃO DOS FRAMES (Estrutura Física)
    // =======================================================
    // O Frame 0 é a base. Os outros frames estão deslocados 0.3m no X local do anterior.
    Frame<double> f1("F1", {0.0, 0.0, 0.0}, {0.0, 0.0, 0.0});
    Frame<double> f2("F2", {0.3, 0.0, 0.0}, {0.0, 0.0, 0.0});
    Frame<double> f3("F3", {0.3, 0.0, 0.0}, {0.0, 0.0, 0.0});
    Frame<double> f_garra("F_Garra", {0.3, 0.0, 0.0}, {0.0, 0.0, 0.0});

    // =======================================================
    // 2. MODELAGEM DAS JUNTAS (Atuadores)
    // =======================================================
    // Usamos make_shared para alocar as juntas e permitir polimorfismo seguro
    auto j1 = make_shared<JuntaRotacional<double>>("J1", f1, 'z');
    auto j2 = make_shared<JuntaRotacional<double>>("J2", f2, 'z');
    auto j3 = make_shared<JuntaRotacional<double>>("J3", f3, 'z');
    auto j_garra = make_shared<JuntaRotacional<double>>("JG", f_garra, 'z'); // Travada (0 rad)

    // =======================================================
    // 3. MONTAGEM DO ROBÔ
    // =======================================================
    vector<shared_ptr<Junta<double>>> juntas = {j1, j2, j3, j_garra};
    RoboArticulado<double> robo("Planar_3R", juntas);

    // =======================================================
    // 4. APLICAÇÃO DOS VALORES (Cinemática Direta)
    // =======================================================
    double val_j1 = -M_PI / 2.0; // +90 deg Horário
    double val_j2 =  M_PI / 2.0; // -90 deg Anti-horário
    double val_j3 = -M_PI / 2.0; // +90 deg Horário
    vector<double> valores_atuacao = {val_j1, val_j2, val_j3, 0.0};

    // =======================================================
    // 5. RESULTADOS
    // =======================================================
    cout << "=== RESULTADOS (MODELO 3D-READY) ===" << endl;

    auto posicoes = robo.getXYZPositions(valores_atuacao);
    
    // Configura o cout para exibir floats com precisão fixa
    cout << fixed;

    for (size_t i = 0; i < posicoes.size(); ++i) {
        // Limpando ruídos de ponto flutuante próximos a zero (ex: -0.00)
        double x = abs(posicoes[i][0]) < 1e-9 ? 0.0 : posicoes[i][0];
        double y = abs(posicoes[i][1]) < 1e-9 ? 0.0 : posicoes[i][1];
        double z = abs(posicoes[i][2]) < 1e-9 ? 0.0 : posicoes[i][2];

        cout << "Ponto " << i << ": X=" << setprecision(2) << x 
             << ", Y=" << setprecision(2) << y 
             << ", Z=" << setprecision(2) << z << endl;
    }

    auto matrizes = robo.forwardKinematics(valores_atuacao);
    auto m_final = matrizes.back(); // Pega o último elemento (a matriz da garra)

    // Calculando a orientação final
    // atan2 em C++ funciona exatamente como np.arctan2 (y, x)
    double phi_rad = atan2(m_final[1][0], m_final[0][0]);
    double phi_deg = phi_rad * (180.0 / M_PI);

    // Limpando possíveis ruídos de ponto flutuante da posição final
    double final_x = abs(m_final[0][3]) < 1e-9 ? 0.0 : m_final[0][3];
    double final_y = abs(m_final[1][3]) < 1e-9 ? 0.0 : m_final[1][3];

    cout << "\n=== RESPOSTA FINAL ===" << endl;
    cout << "x   = " << setprecision(1) << final_x << " m" << endl;
    cout << "y   = " << setprecision(1) << final_y << " m" << endl;
    cout << "phi = " << setprecision(0) << phi_deg << "°" << endl;

    return 0;
}