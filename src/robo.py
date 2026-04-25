from abc import ABC, abstractmethod
import numpy as np
from typing import List
from src.junta import Junta

class Robo(ABC):
    def __init__(self, num_joints: int, num_links: int):
        if not isinstance(num_joints, int) or not isinstance(num_links, int):
            raise TypeError("num_joints and num_links must be integers.")
            
        self.num_joints = num_joints
        self.num_links = num_links
    
    @abstractmethod
    def forward_kinematics(self, joint_values: List[float]) -> List[np.ndarray]:
        pass
    
    @abstractmethod
    def backward_kinematics(self, position_values: List[float]) -> List[np.ndarray]:
        pass


class RoboArticulado(Robo):
    def __init__(self, name: str, joints: List[Junta]):
        if not isinstance(name, str):
            raise TypeError("Robot name must be a string.")
        if not all(isinstance(j, Junta) for j in joints):
            raise TypeError("joints must be a list containing only instances of the Junta class.")
            
        super().__init__(len(joints), len(joints))
        self.name = name
        self.joints = joints

    def forward_kinematics(self, joint_values: List[float]) -> List[np.ndarray]:
        if len(joint_values) != self.num_joints:
            raise ValueError(f"Robot has {self.num_joints} joints, but received {len(joint_values)} actuation values.")

        total_transformation = np.eye(4, dtype=float)
        global_poses = []

        for joint, value in zip(self.joints, joint_values):
            local_transformation = joint.apply_actuation(value)
            total_transformation = total_transformation @ local_transformation
            global_poses.append(total_transformation)

        return global_poses

    def get_xyz_positions(self, joint_values: List[float]) -> List[np.ndarray]:
        poses = self.forward_kinematics(joint_values)
        positions = [np.zeros(3)] 
        
        for matrix in poses:
            positions.append(matrix[0:3, 3])
            
        return positions