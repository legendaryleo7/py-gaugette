import gaugette


A_PIN = input("Please enter A Pin:")
B_PIN = input("Please enter B Bin:")


encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()


while 1:
    delta = encoder.get_delta()
    if delta != 0:
        print "rotated %d" % delta
