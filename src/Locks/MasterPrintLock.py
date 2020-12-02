import threading


class MasterPrintLock:
    PRINT_LOCK = threading.Lock()


master = MasterPrintLock()
worker = MasterPrintLock()
