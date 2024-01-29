#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64MultiArray
from brics_actuator.msg import JointPositions, JointValue

def youbot_joint_publisher(joint_value=[2.9,1.05,-2.44,1.73,2.95]):
    # 初始化ROS节点
    rospy.init_node('youbot_joint_publisher', anonymous=True)

    # 创建一个Publisher，发布JointPositions消息到指定的话题
    joint_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size=10)

    # 设置循环的频率
    rospy.sleep(5)  

    try:
        # 创建JointPositions消息
        joint_positions_msg = JointPositions()

        # 创建JointValue对象，设置关节名称和目标位置

        jv1 = JointValue()
        jv1.joint_uri = "arm_joint_1"
        jv1.value = joint_value[0]
        jv1.unit = "rad"
        
        jv2 = JointValue()
        jv2.joint_uri = "arm_joint_2"
        jv2.value = joint_value[1]
        jv2.unit = "rad"

        jv3 = JointValue()
        jv3.joint_uri = "arm_joint_3"
        jv3.value = joint_value[2]
        jv3.unit = "rad"
        
        jv4 = JointValue()
        jv4.joint_uri = "arm_joint_4"
        jv4.value = joint_value[3]
        jv4.unit = "rad"
        
        jv5 = JointValue()
        jv5.joint_uri = "arm_joint_5"
        jv5.value = joint_value[4]
        jv5.unit = "rad"
        
        
        # 将JointValue添加到JointPositions消息中
        joint_positions_msg.positions.append(jv1)
        joint_positions_msg.positions.append(jv2)
        joint_positions_msg.positions.append(jv3)
        joint_positions_msg.positions.append(jv4)
        joint_positions_msg.positions.append(jv5)
        # 发布消息
        joint_pub.publish(joint_positions_msg)
        return "move_successfullly"

    except Exception:
        return 'arm move failure'
if __name__ == '__main__':
    try:
        youbot_joint_publisher()
        youbot_joint_publisher([0.11,0.11,-0.11,0.11,0.11])
        rospy.sleep(3)
        def myhook():
            print "shutdown time!"

        rospy.on_shutdown(myhook)
    except rospy.ROSInterruptException:
        pass
