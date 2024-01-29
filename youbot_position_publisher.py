#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
from brics_actuator.msg import JointPositions, JointValue

def youbot_joint_publisher():
    # 初始化ROS节点
    rospy.init_node('youbot_joint_publisher', anonymous=True)

    # 创建一个Publisher，发布JointPositions消息到指定的话题
    joint_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size=10)

    # 设置循环的频率
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # 创建JointPositions消息
        joint_positions_msg = JointPositions()

        # 创建JointValue对象，设置关节名称和目标位置
        joint_value = JointValue()
        joint_value.joint_uri = "arm_joint_1"
        joint_value.unit = "rad"  # 单位为弧度
        joint_value.value = 1.0  # 目标关节位置

        # 将JointValue添加到JointPositions消息中
        joint_positions_msg.positions.append(joint_value)

        # 发布消息
        joint_pub.publish(joint_positions_msg)

        # 按照设置的频率休眠
        rate.sleep()

if __name__ == '__main__':
    try:
        youbot_joint_publisher()
    except rospy.ROSInterruptException:
        pass
