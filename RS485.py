from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException
from pymodbus.payload import BinaryPayloadDecoder


# Replace the serial port name with the one connected to your Modbus RTU device
# SERIAL_PORT = '/dev/ttyUSB0'  # For Linux
SERIAL_PORT = 'COM31'       # For Windows

# Function to read a meter register value
def read_meter_register(register_address):
    client = ModbusSerialClient(method='rtu', port=SERIAL_PORT, baudrate=9600, timeout=1)
    
    # Specify the slave address and register address to read from
    slave_address = 1  # Replace with the slave address of your meter
    try:
        if not client.connect():
            raise ModbusIOException("Failed to connect to the Modbus RTU device")
        
        response = client.read_holding_registers(register_address, 1, unit=slave_address)
        # print("Responce is:-", response.register)
        if response.isError():
            print("Modbus Error:", response)
            return None
        else:
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, byteorder='big')
            register_value = decoder.decode_16bit_uint()
            return register_value
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        client.close()

try:
    # Replace 'register_address' with the Modbus address of the meter register you want to read
    register_address = 30008
    meter_value = read_meter_register(register_address)

    if meter_value is not None:
        print(f"Register Value: {meter_value}")

except Exception as e:
    print("Error:", e)
