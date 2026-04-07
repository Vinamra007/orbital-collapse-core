from auth import login
from telemetry import parser
from ground_control import dashboard
from launch_sequence import dispatcher


def check_auth():
    return login.authenticate()


def check_telemetry():
    return parser.parse_signal()


def check_dispatch():
    return dispatcher.dispatch()


def check_ground():
    return dashboard.display_status()


def run_all_checks():
    print(check_auth())
    print(check_telemetry())
    print(check_dispatch())
    print(check_ground())

    print("❌ SYSTEM NOT STABLE")


if __name__ == "__main__":
    run_all_checks()