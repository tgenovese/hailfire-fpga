import unittest

from myhdl import Signal, Simulation, always, concat, delay, downrange, intbv, traceSignals
from random import randrange
from RobotIO import RobotIO
from TestUtils import ClkGen, spi_transfer, LOW, HIGH

def TestBench(RobotIOTester):

    # Create signals with default values
    clk25      = Signal(LOW)

    sspi_clk   = Signal(LOW)
    sspi_cs    = Signal(LOW)
    sspi_miso  = Signal(LOW)
    sspi_mosi  = Signal(LOW)

    rc1_cha    = Signal(LOW)
    rc1_chb    = Signal(LOW)
    rc2_cha    = Signal(LOW)
    rc2_chb    = Signal(LOW)
    rc3_cha    = Signal(LOW)
    rc3_chb    = Signal(LOW)
    rc4_cha    = Signal(LOW)
    rc4_chb    = Signal(LOW)

    mot1_brake = Signal(LOW)
    mot1_dir   = Signal(LOW)
    mot1_pwm   = Signal(LOW)

    mot2_brake = Signal(LOW)
    mot2_dir   = Signal(LOW)
    mot2_pwm   = Signal(LOW)

    mot3_brake = Signal(LOW)
    mot3_dir   = Signal(LOW)
    mot3_pwm   = Signal(LOW)

    mot4_brake = Signal(LOW)
    mot4_dir   = Signal(LOW)
    mot4_pwm   = Signal(LOW)

    mot5_brake = Signal(LOW)
    mot5_dir   = Signal(LOW)
    mot5_pwm   = Signal(LOW)

    mot6_brake = Signal(LOW)
    mot6_dir   = Signal(LOW)
    mot6_pwm   = Signal(LOW)

    mot7_brake = Signal(LOW)
    mot7_dir   = Signal(LOW)
    mot7_pwm   = Signal(LOW)

    mot8_brake = Signal(LOW)
    mot8_dir   = Signal(LOW)
    mot8_pwm   = Signal(LOW)

    adc1_clk   = Signal(LOW)
    adc1_cs    = Signal(LOW)
    adc1_miso  = Signal(LOW)
    adc1_mosi  = Signal(LOW)

    pwm1_ch0   = Signal(LOW)
    pwm1_ch1   = Signal(LOW)
    pwm1_ch2   = Signal(LOW)
    pwm1_ch3   = Signal(LOW)
    pwm1_ch4   = Signal(LOW)
    pwm1_ch5   = Signal(LOW)
    pwm1_ch6   = Signal(LOW)
    pwm1_ch7   = Signal(LOW)

    ext1_0     = Signal(LOW)
    ext1_1     = Signal(LOW)
    ext1_2     = Signal(LOW)
    ext1_3     = Signal(LOW)
    ext1_4     = Signal(LOW)
    ext1_5     = Signal(LOW)
    ext1_6     = Signal(LOW)
    ext1_7     = Signal(LOW)

    ext2_0     = Signal(LOW)
    ext2_1     = Signal(LOW)
    ext2_2     = Signal(LOW)
    ext2_3     = Signal(LOW)
    ext2_4     = Signal(LOW)
    ext2_5     = Signal(LOW)
    ext2_6     = Signal(LOW)
    ext2_7     = Signal(LOW)

    ext3_0     = Signal(LOW)
    ext3_1     = Signal(LOW)
    ext3_2     = Signal(LOW)
    ext3_3     = Signal(LOW)
    ext3_4     = Signal(LOW)
    ext3_5     = Signal(LOW)
    ext3_6     = Signal(LOW)
    ext3_7     = Signal(LOW)

    ext4_0     = Signal(LOW)
    ext4_1     = Signal(LOW)
    ext4_2     = Signal(LOW)
    ext4_3     = Signal(LOW)
    ext4_4     = Signal(LOW)
    ext4_5     = Signal(LOW)
    ext4_6     = Signal(LOW)
    ext4_7     = Signal(LOW)

    ext5_0     = Signal(LOW)
    ext5_1     = Signal(LOW)
    ext5_2     = Signal(LOW)
    ext5_3     = Signal(LOW)
    ext5_4     = Signal(LOW)
    ext5_5     = Signal(LOW)
    ext5_6     = Signal(LOW)
    ext5_7     = Signal(LOW)

    ext6_0     = Signal(LOW)
    ext6_1     = Signal(LOW)
    ext6_2     = Signal(LOW)
    ext6_3     = Signal(LOW)
    ext6_4     = Signal(LOW)
    ext6_5     = Signal(LOW)
    ext6_6     = Signal(LOW)
    ext6_7     = Signal(LOW)

    ext7_0     = Signal(LOW)
    ext7_1     = Signal(LOW)
    ext7_2     = Signal(LOW)
    ext7_3     = Signal(LOW)
    ext7_4     = Signal(LOW)
    ext7_5     = Signal(LOW)
    ext7_6     = Signal(LOW)
    ext7_7     = Signal(LOW)

    # Instanciate module under test
    RobotIO_inst = traceSignals(RobotIO,
        clk25,
        sspi_clk, sspi_cs, sspi_miso, sspi_mosi,
        rc1_cha, rc1_chb,
        rc2_cha, rc2_chb,
        rc3_cha, rc3_chb,
        rc4_cha, rc4_chb,
        mot1_brake, mot1_dir, mot1_pwm,
        mot2_brake, mot2_dir, mot2_pwm,
        mot3_brake, mot3_dir, mot3_pwm,
        mot4_brake, mot4_dir, mot4_pwm,
        mot5_brake, mot5_dir, mot5_pwm,
        mot6_brake, mot6_dir, mot6_pwm,
        mot7_brake, mot7_dir, mot7_pwm,
        mot8_brake, mot8_dir, mot8_pwm,
        adc1_clk, adc1_cs, adc1_miso, adc1_mosi,
        pwm1_ch0, pwm1_ch1, pwm1_ch2, pwm1_ch3, pwm1_ch4, pwm1_ch5, pwm1_ch6, pwm1_ch7,
        ext1_0, ext1_1, ext1_2, ext1_3, ext1_4, ext1_5, ext1_6, ext1_7,
        ext2_0, ext2_1, ext2_2, ext2_3, ext2_4, ext2_5, ext2_6, ext2_7,
        ext3_0, ext3_1, ext3_2, ext3_3, ext3_4, ext3_5, ext3_6, ext3_7,
        ext4_0, ext4_1, ext4_2, ext4_3, ext4_4, ext4_5, ext4_6, ext4_7,
        ext5_0, ext5_1, ext5_2, ext5_3, ext5_4, ext5_5, ext5_6, ext5_7,
        ext6_0, ext6_1, ext6_2, ext6_3, ext6_4, ext6_5, ext6_6, ext6_7,
        ext7_0, ext7_1, ext7_2, ext7_3, ext7_4, ext7_5, ext7_6, ext7_7,
    )

    # Instanciate tester module
    RobotIOTester_inst = RobotIOTester(
        clk25,
        sspi_clk, sspi_cs, sspi_miso, sspi_mosi,
        rc1_cha, rc1_chb,
        rc2_cha, rc2_chb,
        rc3_cha, rc3_chb,
        rc4_cha, rc4_chb,
        mot1_brake, mot1_dir, mot1_pwm,
        mot2_brake, mot2_dir, mot2_pwm,
        mot3_brake, mot3_dir, mot3_pwm,
        mot4_brake, mot4_dir, mot4_pwm,
        mot5_brake, mot5_dir, mot5_pwm,
        mot6_brake, mot6_dir, mot6_pwm,
        mot7_brake, mot7_dir, mot7_pwm,
        mot8_brake, mot8_dir, mot8_pwm,
        adc1_clk, adc1_cs, adc1_miso, adc1_mosi,
        pwm1_ch0, pwm1_ch1, pwm1_ch2, pwm1_ch3, pwm1_ch4, pwm1_ch5, pwm1_ch6, pwm1_ch7,
        ext1_0, ext1_1, ext1_2, ext1_3, ext1_4, ext1_5, ext1_6, ext1_7,
        ext2_0, ext2_1, ext2_2, ext2_3, ext2_4, ext2_5, ext2_6, ext2_7,
        ext3_0, ext3_1, ext3_2, ext3_3, ext3_4, ext3_5, ext3_6, ext3_7,
        ext4_0, ext4_1, ext4_2, ext4_3, ext4_4, ext4_5, ext4_6, ext4_7,
        ext5_0, ext5_1, ext5_2, ext5_3, ext5_4, ext5_5, ext5_6, ext5_7,
        ext6_0, ext6_1, ext6_2, ext6_3, ext6_4, ext6_5, ext6_6, ext6_7,
        ext7_0, ext7_1, ext7_2, ext7_3, ext7_4, ext7_5, ext7_6, ext7_7,
    )

    # Clock generator
    ClkGen_inst = ClkGen(clk25)

    return RobotIO_inst, RobotIOTester_inst, ClkGen_inst

class TestRobotIO(unittest.TestCase):

    def RobotIOTester(self,
                 clk25,
                 sspi_clk, sspi_cs, sspi_miso, sspi_mosi,
                 rc1_cha, rc1_chb,
                 rc2_cha, rc2_chb,
                 rc3_cha, rc3_chb,
                 rc4_cha, rc4_chb,
                 mot1_brake, mot1_dir, mot1_pwm,
                 mot2_brake, mot2_dir, mot2_pwm,
                 mot3_brake, mot3_dir, mot3_pwm,
                 mot4_brake, mot4_dir, mot4_pwm,
                 mot5_brake, mot5_dir, mot5_pwm,
                 mot6_brake, mot6_dir, mot6_pwm,
                 mot7_brake, mot7_dir, mot7_pwm,
                 mot8_brake, mot8_dir, mot8_pwm,
                 adc1_clk, adc1_cs, adc1_miso, adc1_mosi,
                 pwm1_ch0, pwm1_ch1, pwm1_ch2, pwm1_ch3, pwm1_ch4, pwm1_ch5, pwm1_ch6, pwm1_ch7,
                 ext1_0, ext1_1, ext1_2, ext1_3, ext1_4, ext1_5, ext1_6, ext1_7,
                 ext2_0, ext2_1, ext2_2, ext2_3, ext2_4, ext2_5, ext2_6, ext2_7,
                 ext3_0, ext3_1, ext3_2, ext3_3, ext3_4, ext3_5, ext3_6, ext3_7,
                 ext4_0, ext4_1, ext4_2, ext4_3, ext4_4, ext4_5, ext4_6, ext4_7,
                 ext5_0, ext5_1, ext5_2, ext5_3, ext5_4, ext5_5, ext5_6, ext5_7,
                 ext6_0, ext6_1, ext6_2, ext6_3, ext6_4, ext6_5, ext6_6, ext6_7,
                 ext7_0, ext7_1, ext7_2, ext7_3, ext7_4, ext7_5, ext7_6, ext7_7):

        def set_lines(data, l0, l1, l2, l3, l4, l5, l6, l7):
            """ Pull l[0-7] lines high or low to match bits [0-7] of data """
            l0.next = data[0]
            l1.next = data[1]
            l2.next = data[2]
            l3.next = data[3]
            l4.next = data[4]
            l5.next = data[5]
            l6.next = data[6]
            l7.next = data[7]

        def set_ext1_port(data):
            """ Pull ext1_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext1 port'
            set_lines(data, ext1_0, ext1_1, ext1_2, ext1_3, ext1_4, ext1_5, ext1_6, ext1_7)

        def set_ext2_port(data):
            """ Pull ext2_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext2 port'
            set_lines(data, ext2_0, ext2_1, ext2_2, ext2_3, ext2_4, ext2_5, ext2_6, ext2_7)

        def set_ext3_port(data):
            """ Pull ext3_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext3 port'
            set_lines(data, ext3_0, ext3_1, ext3_2, ext3_3, ext3_4, ext3_5, ext3_6, ext3_7)

        def set_ext4_port(data):
            """ Pull ext4_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext4 port'
            set_lines(data, ext4_0, ext4_1, ext4_2, ext4_3, ext4_4, ext4_5, ext4_6, ext4_7)

        def set_ext5_port(data):
            """ Pull ext5_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext5 port'
            set_lines(data, ext5_0, ext5_1, ext5_2, ext5_3, ext5_4, ext5_5, ext5_6, ext5_7)

        def set_ext6_port(data):
            """ Pull ext6_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext6 port'
            set_lines(data, ext6_0, ext6_1, ext6_2, ext6_3, ext6_4, ext6_5, ext6_6, ext6_7)

        def set_ext7_port(data):
            """ Pull ext7_[0-7] lines high or low to match bits [0-7] of data """
            print 'set ext7 port'
            set_lines(data, ext7_0, ext7_1, ext7_2, ext7_3, ext7_4, ext7_5, ext7_6, ext7_7)

        def set_ext_ports(datas):
            """ Pull ext[1-7]_[0-7] lines high or low to match bits [0-7] of datas [1-7] """
            print 'set all ext ports'
            set_ext1_port(datas[1])
            set_ext2_port(datas[2])
            set_ext3_port(datas[3])
            set_ext4_port(datas[4])
            set_ext5_port(datas[5])
            set_ext6_port(datas[6])
            set_ext7_port(datas[7])

        def get_read_ext_port_command(number):
            """ Return an intbv suitable to be sent to the slave to read ext[number] port """
            ret = intbv(0)[24:]
            ret[24:16] = 0x20 + number  # read ext port (1 to 7)
            ret[16:8] = 1               # expect 1 byte
            return ret

        def read_ext_port(number, expected_data):
            """ Read ext[number] port and compare the result byte to expected_data """
            print 'read ext port nb:', number, '...',
            master_to_slave = get_read_ext_port_command(number)
            slave_to_master = intbv(0)
            yield spi_transfer(sspi_miso, sspi_mosi, sspi_clk, sspi_cs, master_to_slave, slave_to_master)
            self.assertEquals(slave_to_master[8:], expected_data)
            print 'done'

        def read_ext_ports(expected_datas):
            """ Read all ext ports in one SPI transfer and compare the result bytes to expected_datas """
            print 'read all ext ports at once...',
            master_to_slave = get_read_ext_port_command(7)
            for i in downrange(7, 1):
                master_to_slave = concat(master_to_slave, get_read_ext_port_command(i))
            slave_to_master = intbv(0)
            yield spi_transfer(sspi_miso, sspi_mosi, sspi_clk, sspi_cs, master_to_slave, slave_to_master)
            for i in downrange(8, 1):
                self.assertEquals(slave_to_master[i*24-16:(i-1)*24], expected_datas[i])
            print 'done'

        def test_ext_ports():
            # Generate random inputs for ext ports
            ext_port_config = [intbv(randrange(0xFF)) for i in range(0, 8) ]

            # Set up ext ports
            set_ext_ports(ext_port_config)

            # Read ext ports separately
            for i in range(1, 8):
                yield read_ext_port(i, ext_port_config[i])

            # Read ext ports together
            yield read_ext_ports(ext_port_config)

        yield test_ext_ports()

    def testRobotIO(self):
        """ Test RobotIO """
        sim = Simulation(TestBench(self.RobotIOTester))
        sim.run(8000)

if __name__ == '__main__':
    unittest.main()