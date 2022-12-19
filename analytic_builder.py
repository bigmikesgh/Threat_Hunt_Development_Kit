# Functions for the analytic builder


class Analytic:
    def __init__(self, name, tactic_id, technique_id, detection_language, query_logic, intel_source,
                 threat_actor, comment):
        self.name = name
        self.tactic_id = tactic_id
        self.technique_id = technique_id
        self.detection_language = detection_language
        self.query_logic = query_logic
        self.intel_source = intel_source
        self.threat_actor = threat_actor
        self.comment = comment


def build_analytic():
    query_logic = []

    name = input("Enter analytic name: ")
    tactic_id = input("Enter MITRE Tactic ID: ")
    technique_id = input("Enter MITRE Technique ID: ")
    detection_language = input("Enter detection language: ")

    print("Enter query logic (Press Enter twice when done): ", end="")
    while True:
        user_input = input()
        if user_input == '':
            break
        else:
            query_logic.append(user_input + '\n')

    query_logic_str = ''.join(query_logic)
    intel_source = input("Enter threat intelligence source: ")
    threat_actor = input("Enter threat actor associated with detection: ")
    comment = input("Comment: ")

    analytic = Analytic(name.title(), tactic_id.upper(), technique_id.upper(), detection_language.upper(),
                        query_logic_str.rstrip('\n'), intel_source, threat_actor.upper(), comment)

    print(f'\nAnalytic Details\n===============================\nTitle: {analytic.name}'
          f'\nMITRE Tactic: {analytic.tactic_id}\nMITRE Technique: {analytic.technique_id}'
          f'\nLanguage: {analytic.detection_language}\nQuery: {analytic.query_logic}\n'
          f'Threat Intel:{analytic.intel_source}\nThreat Actor:{analytic.threat_actor}\nComments:{analytic.comment}' )

    return analytic


def save_analytic(analytic):
    pass
