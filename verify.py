def check_auth():
    return "[AUTH]"  # placeholder

def check_telemetry():
    return "[TELEMETRY]"  # placeholder

def check_dispatch():
    return "[DISPATCH]"  # placeholder

def check_ground():
    return "[GROUND]"  # placeholder


def run_all_checks():
    print(check_auth())
    print(check_telemetry())
    print(check_dispatch())
    print(check_ground())
    print("❌ SYSTEM NOT STABLE")


if __name__ == "__main__":
    run_all_checks()