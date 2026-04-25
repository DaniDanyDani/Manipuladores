#ifndef JUNTA_HPP
#define JUNTA_HPP

#include <string>
#include <array>
#include <cmath>
#include <stdexcept>
#include "frame.hpp"
#include "linealg.hpp"

template<typename dataType>
class Junta
{
protected:
    std::string name;
    Frame<dataType> frame;
    char axis;

    virtual std::array<std::array<dataType, 4>, 4> calcActuationMatrix(dataType value) const = 0;

public:
    Junta(std::string name, Frame<dataType> frame, char axis = 'z') 
        : name(name), frame(frame), axis(axis)
    {
        if (axis != 'x' && axis != 'y' && axis != 'z') {
            throw std::invalid_argument("O eixo de atuacao deve ser 'x', 'y' ou 'z'.");
        }
    }

    virtual ~Junta() {}

    std::string getName() const { return name; }
    char getAxis() const { return axis; }
    Frame<dataType> getFrame() const { return frame; }

    std::array<std::array<dataType, 4>, 4> applyActuation(dataType value) const
    {
        auto frameMatrix = frame.getFrame();
        auto actuationMatrix = calcActuationMatrix(value);
        
        return multiplyMatrix<dataType, 4, 4, 4>(frameMatrix, actuationMatrix);
    }
};

template<typename dataType>
class JuntaRotacional : public Junta<dataType>
{
public:
    JuntaRotacional(std::string name, Frame<dataType> frame, char axis = 'z')
        : Junta<dataType>(name, frame, axis) {}

protected:
    std::array<std::array<dataType, 4>, 4> calcActuationMatrix(dataType angle) const override
    {
        auto transformationMatrix = eye<dataType, 4>();
        
        dataType cos_q = std::cos(angle);
        dataType sin_q = std::sin(angle);

        if (this->axis == 'z') {
            transformationMatrix[0][0] = cos_q;
            transformationMatrix[0][1] = -sin_q;
            transformationMatrix[1][0] = sin_q;
            transformationMatrix[1][1] = cos_q;
        } 
        else if (this->axis == 'y') {
            transformationMatrix[0][0] = cos_q;
            transformationMatrix[0][2] = sin_q;
            transformationMatrix[2][0] = -sin_q;
            transformationMatrix[2][2] = cos_q;
        } 
        else if (this->axis == 'x') {
            transformationMatrix[1][1] = cos_q;
            transformationMatrix[1][2] = -sin_q;
            transformationMatrix[2][1] = sin_q;
            transformationMatrix[2][2] = cos_q;
        }

        return transformationMatrix;
    }
};

#endif