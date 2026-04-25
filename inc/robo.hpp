#ifndef ROBO_HPP
#define ROBO_HPP

#include <string>
#include <vector>
#include <array>
#include <memory>
#include <stdexcept>
#include "junta.hpp"
#include "linealg.hpp"

// ==========================================
// Classe Abstrata Base: Robo
// ==========================================
template<typename dataType>
class Robo
{
protected:
    int num_joints;
    int num_links;

public:
    Robo(int num_joints, int num_links) 
        : num_joints(num_joints), num_links(num_links) {}

    virtual ~Robo() {}

    virtual std::vector<std::array<std::array<dataType, 4>, 4>> forwardKinematics(const std::vector<dataType>& jointValues) const = 0;
    
    virtual std::vector<std::array<std::array<dataType, 4>, 4>> backwardKinematics(const std::vector<dataType>& positionValues) const = 0;
};

// ==========================================
// Classe Derivada: RoboArticulado
// ==========================================
template<typename dataType>
class RoboArticulado : public Robo<dataType>
{
private:
    std::string name;
    std::vector<std::shared_ptr<Junta<dataType>>> joints;

public:
    RoboArticulado(std::string name, std::vector<std::shared_ptr<Junta<dataType>>> joints)
        : Robo<dataType>(joints.size(), joints.size()), name(name), joints(joints) {}

    std::vector<std::array<std::array<dataType, 4>, 4>> forwardKinematics(const std::vector<dataType>& jointValues) const override
    {
        if (jointValues.size() != this->num_joints) {
            throw std::invalid_argument("Erro: Quantidade de valores recebidos nao corresponde ao numero de juntas.");
        }

        auto totalTransformation = eye<dataType, 4>();
        std::vector<std::array<std::array<dataType, 4>, 4>> globalPoses;
        globalPoses.reserve(this->num_joints);

        for (size_t i = 0; i < this->joints.size(); ++i) {
            auto localTransformation = this->joints[i]->applyActuation(jointValues[i]);
            totalTransformation = multiplyMatrix<dataType, 4, 4, 4>(totalTransformation, localTransformation);
            globalPoses.push_back(totalTransformation);
        }

        return globalPoses;
    }

    std::vector<std::array<dataType, 3>> getXYZPositions(const std::vector<dataType>& jointValues) const
    {
        auto poses = forwardKinematics(jointValues);
        std::vector<std::array<dataType, 3>> positions;
        positions.reserve(poses.size() + 1);

        positions.push_back({0, 0, 0});

        for (const auto& matrix : poses) {
            positions.push_back({matrix[0][3], matrix[1][3], matrix[2][3]});
        }

        return positions;
    }

    std::vector<std::array<std::array<dataType, 4>, 4>> backwardKinematics(const std::vector<dataType>& positionValues) const override
    {
        throw std::logic_error("Erro: Cinemática Inversa (backwardKinematics) ainda não foi implementada.");
    }
};

#endif