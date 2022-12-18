# Functions for the analytic builder

def build_analytic():
    name = input("Enter analytic name: ")
    tactic = input("Enter MITRE Tactic ID: ")
    technique = input("Enter MITRE Technique ID")
    detection_language = input("Enter detection language (SIGMA, KQL, etc.): ")
    analytic = input("Enter analytic:")
    print('Need to create a way to write analytic out to either a file or data base')
