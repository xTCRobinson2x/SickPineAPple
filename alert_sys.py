from win10toast import ToastNotifier
import compare
import threading
# Checks current connection and displays coorispnding alert
def alert():
    toaster = ToastNotifier()
    if compare.compare_to_known() == True:
        toaster.show_toast("Known Network", "You are connected to a known network", threaded=True,
                           icon_path="pineapple_sick.ico")
    else:
        toaster.show_toast("UNKNOWN NETWORK", "ALERT - You are connected to an unknown network", threaded=True,
                           icon_path="pineapple_sick.ico")

# Runs every 5 Minutes to check network connection and notify if unknown connection
def constant():
    toaster = ToastNotifier()
    if compare.compare_to_known() == True:
        pass
    else:
        toaster.show_toast("UNKNOWN NETWORK", "ALERT - You are connected to an unknown network", threaded=True,
                           icon_path="pineapple_sick.ico")
    threading.Timer(300, constant).start()