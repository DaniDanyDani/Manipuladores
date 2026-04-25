#ifndef FRAME_HPP
#define FRAME_HPP

#include <string>
#include <array>
#include <cmath>
#include "linealg.hpp"

template<typename dataType>
class Frame
{
private:
    std::string frameName;
    std::array<std::array<dataType, 4>, 4> frameMatrix;

public:
    Frame()
    {
        setName("{0}");
        setFrame(eye<dataType, 4>()); 
    }
    
    Frame(std::string name, std::array<dataType, 3> origin, std::array<dataType, 3> rpy)
    {
        setName(name);
        buildFrame(origin, rpy);
    }
    
    ~Frame() {}

    std::array<std::array<dataType, 4>, 4> getFrame() const { return frameMatrix; }
    void setFrame(const std::array<std::array<dataType, 4>, 4>& newFrame) { frameMatrix = newFrame; }

    std::string getName() const { return frameName; }
    void setName(const std::string& name) { frameName = name; }

    int buildFrame(std::array<dataType, 3> origin, std::array<dataType, 3> rpy)
    {
        dataType roll = rpy[0];
        dataType pitch = rpy[1];
        dataType yaw = rpy[2];

        std::array<std::array<dataType, 3>, 3> rx = {{
            {1, 0, 0},
            {0, std::cos(roll), -std::sin(roll)},
            {0, std::sin(roll), std::cos(roll)}
        }};
                                                 
        std::array<std::array<dataType, 3>, 3> ry = {{
            {std::cos(pitch), 0, std::sin(pitch)},
            {0, 1, 0},
            {-std::sin(pitch), 0, std::cos(pitch)}
        }};
                                                 
        std::array<std::array<dataType, 3>, 3> rz = {{
            {std::cos(yaw), -std::sin(yaw), 0},
            {std::sin(yaw), std::cos(yaw), 0},
            {0, 0, 1}
        }};

        auto rotationMatrix = multiplyMatrix(rz, ry);
        rotationMatrix = multiplyMatrix(rotationMatrix, rx);
        
        auto newFrame = eye<dataType, 4>();
        
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                newFrame[i][j] = rotationMatrix[i][j];
            }
            newFrame[i][3] = origin[i];
        }
        
        setFrame(newFrame);
        return 0;
    }
};

#endif