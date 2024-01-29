#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import torch
from std_msgs import Float64MultiArray
from brics_actuator.msg import JointPositions,JointValue
import numpy as np
# class ICNNNetworkPolicy:
# 	def __init__(self,model_path):
# 		self.icnn_model = torch.load(model_path)
# 		self.icnn_model.eval()
# 	def generate_action(self, observation):
# 		with torch.icnn_model(observation):
# 			action = self.icnn_model(observation)
# 		return action.numpy
def youbot_joint_publisher():
	rospy.init_node("youbot_joint_publisher")
	joint_pub = rospy

def main():
	rospy.init_node('icnn_policy_publisher')
	rate = rospy.Rate(10)
	policy = ICNNNetworkPolicy("policy.pth")
	pub = rospy.Publisher("")