import threading


class MasterPrintLock:
    PRINT_LOCK = threading.Lock()


worker = MasterPrintLock()
