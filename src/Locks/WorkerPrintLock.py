import threading


class WorkerPrintLock:
    """ This class is used to create the *common object* across
    the files for the **worker code** to share the ```PRINT_LOCK```, so that
    there are **no race condition**, i.e. in this case *garbled text* on the
    CLI output, due to multiple threads trying to print onto the CLI, all at
    once.
    """
    PRINT_LOCK = threading.Lock()


worker = WorkerPrintLock()
