import reports
import sys


def start():
    if (len(sys.argv) > 0):
        if (sys.argv[1] == "pull-reports"):
            reports.pull_reports()
        elif (sys.argv[1] == "pull-recordings"):
            pull_recordings()
        elif (sys.argv[1] == "merge-reports" and len(sys.argv) > 1):
            reports.merge_reports(sys.argv[2])
        else:
            print("Command not recognized.")
    else:
        print("Start pulling Zoom reports by choosing one of the options:\n pull-reports, pull-recordings, merge-reports")

def pull_recordings():
    print("Pull recordings coming soon.")

start()
