# def main():
#     contatos = 33 / 3
#     quantidade = 2
#     print(30 % 2)
#     print(round((11/2)-0.5))
#
# if __name__ == "__main__":
#     main()
#



# def comer():
#     print('gizelli')
#     time.sleep(5)
#     print('thiago')
#     pass
#
# #####################################
# timeout = 10.0 # Sixty seconds
# def doWork():
#     comer()
#
#
# l = task.LoopingCall(doWork)
# l.start(timeout) # call every sixty seconds
#
# reactor.run()

from datetime import datetime
import time

# now1 = datetime.now()
# while True:
#     current_time = now1.strftime("%H:%M:%S")
#     print("Current Time =", current_time)
#
#     now2 = datetime.now()
#     current_time2 = now2.strftime("%H:%M:%S")
#     print("Current Time =", current_time2)
#
#     seconds = int((now2 - now1).total_seconds())
#     print(seconds)
#     if seconds == 5:
#         now3 = datetime.now()
#         current_time3 = now3.strftime("%H:%M:%S")
#         print("Stop -> Current Time =", current_time3)
#         break
#
#
#
from tags.tag import Tag


def main():
    print(Tag.QRCODE_SCANNER.value)

if __name__ == "__main__":
    main()