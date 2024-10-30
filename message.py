from rich.console import Console

console = Console()


def print_info_message(message):
    console.print(message, style="rgb(0,0,255)")

def print_alert_message(message):
    console.print(message, style="rgb(255,0,0)")

def print_warning_message(message):
    console.print(message, style="rgb(255,255,204)")

