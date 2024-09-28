import numpy as np

class Node:
    id = 0                                  #The ID of each Node
    time_left = 0                           #The time left for transmission when a node is in transmitting state
    retransmission_time = 0                 #The time that a node will retransmit after a collision
    retransmission_num = 0                  #The number of retransmissions for each self. Should be less that 40         
    RX_delay1_ends = 0                      #The moment of time when the RX delay ends and the waiting-for-ack state begins
    timeout_ends = 0                        #The moment of time when the timeout for ack waiting is over. 
    collided = False
    ack_received = False
    timeout_for_ack = 0
    duty_cycle = 0
    Toff = 0


    
    def __init__(self, node_ID, ToA, duty_cycle):       #Node instance constructor
        self.id = node_ID
        self.time_left = ToA
        self.retransmission_time = 0
        self.retransmission_num = 0
        self.RX1_delay1_ends = 0
        self.timeout_ends = 0
        self.collided = False
        self.ack_received = False
        self.timeout_for_ack = 0
        self.duty_cycle = duty_cycle
        self.Toff = ToA /self.duty_cycle #> ToA/duty_cycle - ToA
    
    def set_initial_state(self, ToA):
        self.time_left = ToA
        self.retransmission_num = 0
        self.RX_delay1_ends = 0
        self.timeout_ends = 0
        self.collided = False
        self.ack_received = False
        self.timeout_for_ack = 0
        self.Toff = 0

    
    def set_retransmitting_state(self, time, ToA):
        self.time_left = ToA
        self.retransmission_num += 1
        self.retransmission_time = time + int(max(np.random.randint(ToA/self.duty_cycle - ToA, ToA/self.duty_cycle - ToA + 5000), 1))
        self.RX_delay1_ends = 0
        self.timeout_ends = 0
        self.collided = False
        self.ack_received = False
        self.timeout_for_ack = 0
        self.Toff = 0
    
