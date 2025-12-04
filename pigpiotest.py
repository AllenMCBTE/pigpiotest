import pigpio
import time

PIN = 18

print("Connecting to pigpio daemon...")
pi = pigpio.pi()

if not pi.connected:
    print("Failed to connect to pigpio daemon!")

else:
    print("Successfully connected to pigpio daemon")

    try:
        pi.set_mode(PIN, pigpio.OUTPUT)
    except Exception as e:
        print('Failed to set output port: ', str(e))
    else:
        print(f"GPIO {PIN} successfully set as the output port")
        
    try:
        pi.set_PWM_frequency(PIN, 1000)
        pi.set_PWM_dutycycle(PIN, 128)
    except Exception as e:
        print('Failed to set PWM: ', str(e))
    else:
        print('PWM successfully set')

    try:
        time.sleep(2)
        pi.set_PWM_dutycycle(PIN, 0)
    except Exception as e:
        print('Exception occured while running PWM: ', str(e))
    else:
        print('PWM ran for 2 secs without any exception')

    try:
        print("Pin status fetched: ", pi.read(PIN))
    except Exception as e:
        print('Failed to access pin status')

    print("Disconnecting pigpio daemon")
    pi.stop()