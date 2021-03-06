from myhdl import instance, instances, intbv
from Robot.Utils.Constants import LOW, HIGH, CLK_FREQ

def ServoDriver(pwm, clk25, consign, rst_n, optocoupled):
    """

    PWM signal generator for servo motors

    Uses a 25 MHz clock to generate a PWM suitable for servo motors.

    Servo motors work best with a 50 Hz PWM. On this 20 ms period, the
    following duty cycle values are the only ones really useful:
     * 0 ms: servo motor is disabled
     * approximately 1.5 ms: servo motor is at 0 deg
     * approximately 0.5 ms: servo motor is at full right (or left?)
     * approximately 2.5 ms: servo motor is at full left (or right?)
     * all values between 0.5 ms and 2.5 ms.

    In particular, all values beyond 2.5 ms are useless and only induce
    jitter on the servo position. A clock cycle being 0.04 us, 2.5 ms is
    62500 clock cycles. This mean that the useful duty cycle values can
    all be reached with the fullest precision possible with a 16-bit duty
    cycle consign (0 to 65535, with values from 1 to 12500 and from 62500
    to 65535 being useless).

    pwm

        Output PWM signal

    clk25

        25 MHz clock input

    consign

        16-bit unsigned consign value in clock ticks

    rst_n

        Active low reset input (resets internal counter when active).
        Use the consign input to reset the position of the servo.

    optocoupled

        Set to True if output should be inverted to account for optocoupler.

    """

    assert consign.min >= 0 and consign.max <= 2**16, 'wrong consign constraints'

    # account for optocouplers
    LOW_OPTO  = LOW if not optocoupled else HIGH
    HIGH_OPTO = HIGH if not optocoupled else LOW

    PWM_FREQ = 50
    CNT_MAX = int(CLK_FREQ/PWM_FREQ - 1)

    @instance
    def DriveServo():
        """ Generate PWM for servo """

        # cnt overflows at 50Hz
        cnt = intbv(0, min = 0, max = CNT_MAX + 1)

        # 16-bit duty cycle
        duty_cycle = intbv(0)[16:]

        while True:
            yield clk25.posedge, rst_n.negedge
            if rst_n == LOW:
                cnt[:] = 0
                duty_cycle[:] = 0
                pwm.next = LOW_OPTO
            else:
                # accept new consign at the beginning of a period
                if cnt == 0:
                    duty_cycle[:] = consign

                # reached consign?
                if cnt >= duty_cycle:
                    pwm.next = LOW_OPTO
                else:
                    pwm.next = HIGH_OPTO

                if cnt == CNT_MAX:
                    cnt[:] = 0
                else:
                    cnt += 1

    return instances()
