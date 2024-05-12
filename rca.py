
#definining variables

def get_input(prompt):
    return input(prompt)

def get_incident_details():
    incident_details = {}
    
    while True:
        incident_details[1] = get_input("1. What is the AAs login?:")
        if len(incident_details[1]) < 1:
            print("Please provide a valid response")
        else: 
            aa_login = incident_details[1]
            break

    while True:
        incident_details[2] = get_input("2. What was the AAs hire date?:")
        if len(incident_details[2]) < 1:
            print("Please provide a valid response")
        else: 
            hire_date = incident_details[2]
            break

    while True:
        incident_details[3] = get_input('3. When was the AA initially trained in the said process?:')
        if len(incident_details[3]) < 1:
            print("Please provide a valid response")
        else: 
            initial_training_date = incident_details[3]
            break
    
    while True:
        incident_details[4] = get_input("4. What date did the incident occur?:")
        if len(incident_details[4]) < 1:
            print("Please provide a valid response")
        else: 
            incident_date = incident_details[4]
            break

    while True:
        incident_details[5] = get_input("5. At approx. what time did the incident occur?:")
        if len(incident_details[5]) < 1:
            print("Please provide a valid response")
        else: 
            incident_time = incident_details[5]
            break

    while True:
        incident_details[6] = get_input("6. Where was first contact with the injured AA made? (e.g. Wellness Center):")
        if len(incident_details[6]) < 1:
            print("Please provide a valid response")
        else: 
            first_contact = incident_details[6]
            break

    
    while True:
        incident_details[7] = get_input("7. How was the AM first notified of the incident? (e.g. radio):")
        if len(incident_details[7]) < 1:
            print("Please provide a valid response")
        else: 
            notification_method = incident_details[7]
            break
    
    while True:
        incident_details[8] = get_input("8. Who notified the AM? (e.g. login):")
        if len(incident_details[8]) < 1:
            print("Please provide a valid response")
        else: 
            notifier = incident_details[8]
            break

    while True:
        incident_details[9] = get_input("9. What process was the AA working in? (e.g. Pack Smalls:")
        if len(incident_details[9]) < 1:
            print("Please provide a valid response")
        else: 
            process_path = incident_details[9]
            break

    while True:
        incident_details[10] = get_input("10. What body part did the AA injure?:")
        if len(incident_details[10]) < 1:
            print("Please provide a valid response")
        else: 
            body_part = incident_details[10]
            break

    while True:
        incident_details[11] = get_input(f"11. At the time of the incident, how long had the AA been working in {incident_details[9]}?:")
        if len(incident_details[11]) < 1:
            print("Please provide a valid response")
        else: 
            process_path_duration = incident_details[11]
            break
    
    
    while True:
        incident_details[12] = get_input("12. At time of incident, was the AA working overtime? [Y/N]:").strip().lower()  
        if incident_details[12] == "y":
            overtime_status = "was" 
            break
        elif incident_details[12] == "n":
            overtime_status = "was not"
            break
        else:
            print("Please enter [Y/N].")
        
    
    while True:
        incident_details[13] = get_input("13. Is the AA currently working voluntary/mandatory overtime? [Y/N]:").strip().lower()  # Get user input and convert to lowercase
        if incident_details[13] == "y":
            current_overtime_status = "is"
            break
        elif incident_details[13] == "n":
            current_overtime_status = "is not"
            break
        else:
            print("Please enter [Y/N].")


    while True:
        incident_details[14] = get_input("14. Please provide a detailed summary of the incident (min. 140 characters):")
        if len(incident_details[14]) < 140:
            print("Try again. Response must be at least 140 characters long.")
        else:
            detailed_account = incident_details[14]
            break
            
                
    while True:     
        try:
            incident_details[15] = int(get_input("15. On a scale of 1-10, what was the AA's initial discomfort level?:"))
            if 1 <= incident_details[15] <= 10:
                discomfort_level = incident_details[15]
                break
        except ValueError: 
            print("Invalid input. Please enter a valid number.")


    while True:
        incident_details[16] = get_input("16. Does the task have an associated PMV/Standard? [Y/N]:").strip().lower()  # Get user input and convert to lowercase
        if incident_details[16] == "y":
            pmv_standard = "does"
            break
        elif incident_details[16] == "n":
            pmv_standard = "does not"
            break
        else:
            print("Please enter [Y/N].")


    while True:
        incident_details[17] = get_input("17. Was the AA trained according to the PMV/Standard? [Y/N].:").strip().lower()  
        if incident_details[17] == "y":
           pmv_training = "was" 
           break
        elif incident_details[17] == "y":
            pmv_training = "was not"
            break
        else:
            print("Please enter [Y/N].")


    while True:
        incident_details[18] = get_input("18. Was the task being performed in accordance with the PMV/Standard? [Y/N].:").strip().lower()  # Get user input and convert to lowercase
        if incident_details[18] == "y":
            pmv_accordance = "was" 
            break
        elif incident_details[18] == "n":
            pmv_accordance = "was not"
            break
        else:
            print("Please enter [Y/N].")

    while True: 
        incident_details[19] = get_input("19. Was the work area cluttered or congested? [Y/N].:").strip().lower()
        if incident_details[19] == "y":
            work_area = "was"
            break
        elif incident_details[19] == "n":
            work_area = "was not"
            break
        else:
            print("Please enter [Y/N].")


    while True: 
        incident_details[20] = get_input("20. Was the area properly 5S'd? [Y/N].:").strip().lower()
        if incident_details[20] == "y":
            _5s = "was"
            break
        elif incident_details[20] == "n":
            _5s = "was not"
            break
        else: 
            print("Please enter [Y/N].")


    while True: 
        incident_details[21] = get_input("21. Did the AA participate in pre-shift stretches? [Y/N].").strip().lower()
        if incident_details[21] == "y":
            stretches = "did"
            break
        elif incident_details[21] == "n":
            stretches = "did not"
            break
        else: 
            print("Please enter [Y/N].")

    while True: 
        incident_details[22] = get_input("22. Did the process path require job rotation? [Y/N].:").strip().lower()
        if incident_details[22] == "y":
            job_rotation = "was"
            break
        elif incident_details[22] == "n":
            job_rotation = "was not"
            break
        else: 
            print("Please enter [Y/N].")


    while True: 
        incident_details[23] = get_input("23. Was proper job rotation followed? [Y/N].:").strip().lower()
        if incident_details[23] == "y":
            rotation_result = "was"
            break
        elif incident_details[23] == "n":
            rotation_result = "was not"
            break
        else: 
            print("Please enter [Y/N].")

    while True: 
        incident_details[24] = get_input("24. Was the associate being labor shared? [Y/N]:").strip().lower()
        if incident_details[24] == "y":
            labor_share_status = "was"
            break
        elif incident_details[24] == "n":
            labor_share_status = "was not"
            break
        else: 
            print("Please enter [Y/N].")

    while True: 
        incident_details[25] = get_input("25. Was the AA wearing proper PPE? [Y/N].:").strip().lower()
        if incident_details[25] == "y":
            ppe = "was"
            break
        elif incident_details[25] == "n":
            ppe = "was not"
            break
        else: 
            print("Please enter [Y/N].")

    
    while True: 
        incident_details[26] = get_input("26. Was the AA following proper safety policy? [Y/N]").strip().lower()
        if incident_details[26] == "y":
            safety_policy = "was"
            break
        elif incident_details[26] == "n":
            safety_policy = "was not"
            break
        else: 
            print("Please enter [Y/N].")
    
    while True:     
        try:
            incident_details[27] = int(get_input("27. On a scale of 1-10, what was the AA's discomfort level? (post-treatment):"))
            if 1 <= incident_details[27] <= 10:
                break
        except ValueError: 
            print("Invalid input. Please enter a valid number.")

    while True:
        incident_details[28] = get_input("28. Describe how the AA is doing (post-treatment) (min. 140 characters)?:\n")
        if len(incident_details[28]) < 140:
            print("Try again. Response must be at least 280 characters long.")
        else:
            post_treatment = incident_details[28]
            break


    print(f"On {incident_date} at {incident_time} the AM on duty was notified via {notification_method} by {notifier}") 
    print(f"that {aa_login} was in need of Wellness Center assistance. The AM proceeded to {first_contact}. Upon arrival the AM") 
    print(f"found {aa_login} reporting discomfort in their {body_part}. The discomfort began while {aa_login} worked in {process_path}")       
    print(f"The associate has a start date of {hire_date} , and was initially trained in the process on {initial_training_date}")
    print(f"The associate had been performing this process for {process_path_duration}. The associate {overtime_status} working")
    print(f"overtime at the time of the incident. This task {pmv_standard} have an associated PMV/Standard, and the associate")
    print(f"{pmv_training} trained to the PMV/Standard. The task {pmv_accordance} being performed per the PMV/Standard. The associate")
    print(f"reported a discomfort level at time of incident of {discomfort_level}.The work area {work_area} cluttered or congested,")
    print(f"and everything {_5s} in its proper 5S location. The AA {stretches} participate in pre-shift stretching exercises.")
    print(f"The associate was working in {process_path} and {job_rotation} working in a process path that requires job rotation") 
    print(f"and the investigation determined that proper job rotation {rotation_result} being followed. The associate {labor_share_status}") 
    print(f"currently being labor shared and had been working in the process path for {process_path_duration}.The investigation") 
    print(f"identified that the associate {ppe} wearing their PPE at the time of the incident and {safety_policy} found to be following")
    print(f"Amazon safety policy/procedure (PMV, Safety Standard of Conduct, etc.) The associate {current_overtime_status} currently")
    print(f"working voluntary/mandatory overtime. The AA received conservative treatment in Wellness Center, and reported a discomfort")
    print(f"level of {incident_details[27]} after treatment.\n")

    print(f"The AA gave the following account of the incident:")
                
    print(f"{detailed_account}\n") 

    print(f"Post-Treatment Assesment\n {incident_details[28]}")


def main():
    get_incident_details()

main()


#use Github link to share this project

