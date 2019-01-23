from pyme31 import Me31

def main():
    dmm = Me31('COM4')

    for i in range (5):
        measurment = dmm.get_measurment()
        print(measurment)
        print(measurment.value)
        print(measurment.unit)
        print(measurment.measuring_mode)

if __name__ == "__main__":
    main()