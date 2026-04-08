def validate_signal(signal):
    if signal is None:
        return False
    if not isinstance(signal, (str, dict, list)):
        return False
    return len(str(signal)) > 0