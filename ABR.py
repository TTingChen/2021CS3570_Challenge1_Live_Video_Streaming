# import tensorflow as tf
#NN_MODEL = "./submit/results/nn_model_ep_18200.ckpt" # model path settings, if using ML-based method
TARGET_BUFFER = [0.6 , 1.0]

class Algorithm:
     def __init__(self):
     # fill your self params
        self.some_param = 0
    
     # Initail
     def Initial(self):
     # Initail your session or something
        self.some_param = 0

    def playback_ctrl(self, buffer_occupy):
        # after rounding 0.6 / 2 = 0.3
        b0_min = round(TARGET_BUFFER[0]/2, 1)
        b0_max = TARGET_BUFFER[0]*2
        b1_min = round(TARGET_BUFFER[1]/2, 1)
        b1_max = TARGET_BUFFER[1]*2

        # calculate target buffer
        if(buffer_occupy >= b0_min and buffer_occupy < b0_max):
            t_buffer = 1
        else:
            t_buffer = 0

        # calculate the corresponding playback rate
        if(buffer_occupy < b0_min):
            play_rate = 0.95
        elif(buffer_occupy >=  b0_max):
            play_rate = 1.05
        else:
            play_rate = 1
        
        return t_buffer, play_rate

     # Define your algo
     def run(self, time, S_time_interval, S_send_data_size, S_chunk_len, S_rebuf, S_buffer_size, S_play_time_len,S_end_delay, S_decision_flag, S_buffer_flag,S_cdn_flag,S_skip_time, end_of_video, cdn_newest_id,download_id,cdn_has_frame,IntialVars):

         # If you choose the marchine learning
         '''state = []

         state[0] = ...
         state[1] = ...
         state[2] = ...
         state[3] = ...
         state[4] = ...

         decision = actor.predict(state).argmax()
         bit_rate, target_buffer = decison//4, decison % 4 .....
         return bit_rate, target_buffer'''

         # If you choose BBA
         # Playback Rate control
         target_buffer, play_rate = self.playback_ctrl(S_buffer_size[-1])

         # Segment Bitrate control
         
         # Bitrate control
         RESEVOIR = 0.5
         CUSHION =  1.5
         
         if S_buffer_size[-1] < RESEVOIR:
             bit_rate = 0    
         elif S_buffer_size[-1] >= RESEVOIR + CUSHION and S_buffer_size[-1] < CUSHION +CUSHION:
             bit_rate = 2
         elif S_buffer_size[-1] >= CUSHION + CUSHION:
             bit_rate = 3
         else:
             bit_rate = 1

         # Frame dropping control
         latency_limit = 4



         return bit_rate, target_buffer, latency_limit

         # If you choose other
         #......



     def get_params(self):
     # get your params
        your_params = []
        return your_params
