import time

class TimeError(Exception):
    """A costume exception used to report errors in use of Timer class"""

class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        """Star a new timer"""
        if self._start_time is not None:
            raise TimeError('Timer is runnung, use .stop() to stop it.')
        self._start_time = time.perf_counter()

    def stop(self):
        """Stop a the timer and report the elapsed time"""
        if self._start_time is None:
            raise TimeError('Timer is not runnung, use .start() to start it.')

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
