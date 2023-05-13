# Desc: A program to organize patient data using multiple functions 
# Inputs: You can input a number using the list provided, or input new patient data
# Output: It will output certain patient data and statistics based on your input


import datetime
from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    
    patients = {}
    try:
        with open(fileName, 'r') as file:
            for line in file:
                try:
                    fields = line.strip().split(',')
                    if len(fields) != 8:
                        raise ValueError(f"Invalid number of fields ({len(fields)}) in line: {line.strip()}")

                    patientId = int(fields[0])
                    date = fields[1].strip()
                    temperature = float(fields[2])
                    heartRate = int(fields[3])
                    respiratoryRate = int(fields[4])
                    systolicBP = int(fields[5])
                    diastolicBP = int(fields[6])
                    oxygenSaturation = int(fields[7])

                    if not (35 <= temperature <= 42):
                        raise ValueError(f"Invalid temperature value ({temperature}) in line: {line.strip()}")
                    if not (30 <= heartRate <= 180):
                        raise ValueError(f"Invalid heart rate value ({heartRate}) in line: {line.strip()}")
                    if not (5 <= respiratoryRate <= 40):
                        raise ValueError(f"Invalid respiratory rate value ({respiratoryRate}) in line: {line.strip()}")
                    if not (70 <= systolicBP <= 200):
                        raise ValueError(f"Invalid systolic blood pressure value ({systolicBP}) in line: {line.strip()}")
                    if not (40 <= diastolicBP <= 120):
                        raise ValueError(f"Invalid diastolic blood pressure value ({diastolicBP}) in line: {line.strip()}")
                    if not (70 <= oxygenSaturation <= 100):
                        raise ValueError(f"Invalid oxygen saturation value ({oxygenSaturation}) in line: {line.strip()}")

                    if patientId not in patients:
                        patients[patientId] = []
                    patients[patientId].append([date, temperature, heartRate, respiratoryRate, systolicBP, diastolicBP, oxygenSaturation])

                except ValueError as e:
                    print(str(e))
                    continue

    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    except:
        print("An unexpected error occurred while reading the file.")

    return patients


def displayPatientData(patients, patientId=0):
   
    # Check if patients is a dictionary
    if not isinstance(patients, dict):
        print("Error: patients must be a dictionary")
        return

    # Check if patientId is an integer
    if not isinstance(patientId, int):
        print("Error: patientId must be an integer")
        return

    # Check if patientId is negative
    if patientId < 0:
        print("Error: patientId must be a non-negative integer")
        return

    # Check if patientId is in patients
    if patientId != 0 and patientId not in patients:
        print(f"Patient with ID {patientId} not found.")
        return

    # Display data for each patient
    for patient_id, patient_data in patients.items():
        if patientId == 0 or patient_id == patientId:
            print(f"Patient ID: {patient_id}")
            for visit in patient_data:
                print(f"Visit Date: {visit[0]}")
                print(f"Temperature: {visit[1]}")
                print(f"Heart Rate: {visit[2]}")
                print(f"Respiratory Rate: {visit[3]}")
                print(f"Systolic Blood Pressure: {visit[4]}")
                print(f"Diastolic Blood Pressure: {visit[5]}")
                print(f"Oxygen Saturation: {visit[6]}")
            print("\n")


def displayStats(patients, patientId=0 ):
    # Check that patients is a dictionary
    if not isinstance(patients, dict):
        print("Error: 'patients' should be a dictionary.")
        return

    # Check that patientId is an integer
    if not isinstance(patientId, int):
        print("Error: 'patientId' should be an integer.")
        return
    
    if patientId == 0:
        
        num_patients = len(patients)        
              
        if num_patients == 0:
            print("No data found")
            return

        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = num_visits = 0
        for patientId, visits in patients.items():
            for visit in visits:
                num_visits = num_visits + 1
                temp_sum += visit[1] #Temp 
                hr_sum += visit[2] #heart rate
                rr_sum += visit[3] #respiratory_rate
                sbp_sum += visit[4] #systolic_bp
                dbp_sum += visit[5] #'diastolic_bp'
                spo2_sum += visit[6] #spo2

        avg_temp = temp_sum / num_visits
        avg_hr = hr_sum / num_visits
        avg_rr = rr_sum / num_visits
        avg_sbp = sbp_sum / num_visits
        avg_dbp = dbp_sum / num_visits
        avg_spo2 = spo2_sum / num_visits

        print("Vital Signs for All Patients:")
        print("  Average temperature:", "%.2f" % avg_temp, "C")
        print("  Average heart rate:", "%.2f" % avg_hr, "bpm")
        print("  Average respiratory rate:", "%.2f" % avg_rr, "bpm")
        print("  Average systolic blood pressure:", "%.2f" % avg_sbp, "mmHg")
        print("  Average diastolic blood pressure:", "%.2f" % avg_dbp, "mmHg")
        print("  Average oxygen saturation:", "%.2f" % avg_spo2, "%")

    else:
        if patientId != 0 and patientId not in patients:
           print("No data found for patient with ID {}.".format(patientId))
           return 
        else:
            temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = num_visits = 0
            for patient_id, patient_data in patients.items():
                if patientId == 0 or patient_id == patientId:
                #print(f"Patient ID: {patient_id}")
                    for visit in patient_data:
                        num_visits = num_visits + 1
                        temp_sum += visit[1] #Temp 
                        hr_sum += visit[2] #heart rate
                        rr_sum += visit[3] #respiratory_rate
                        sbp_sum += visit[4] #systolic_bp
                        dbp_sum += visit[5] #'diastolic_bp'
                        spo2_sum += visit[6] #spo2

            avg_temp = temp_sum / num_visits
            avg_hr = hr_sum / num_visits
            avg_rr = rr_sum / num_visits
            avg_sbp = sbp_sum / num_visits
            avg_dbp = dbp_sum / num_visits
            avg_spo2 = spo2_sum / num_visits

            print("Vital Signs for Patient: [", patientId, "]" )
            print("  Average temperature:", "%.2f" % avg_temp, "C")
            print("  Average heart rate:", "%.2f" % avg_hr, "bpm")
            print("  Average respiratory rate:", "%.2f" % avg_rr, "bpm")
            print("  Average systolic blood pressure:", "%.2f" % avg_sbp, "mmHg")
            print("  Average diastolic blood pressure:", "%.2f" % avg_dbp, "mmHg")
            print("  Average oxygen saturation:", "%.2f" % avg_spo2, "%")

        
def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
   
    try:
        # Check that patientId is an integer
        patientId = int(patientId)
    except ValueError:
        print("Invalid patient ID. Please enter an integer value.")
        return
    
    try:
        # Check that date is valid and in the format 'yyyy-mm-dd'
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
        return

    try:
        # Check that temperature is a float between 35.0 and 42.0 Celsius
        temp = float(temp)
        if not (35.0 <= temp <= 42.0):
            raise ValueError
    except ValueError:
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return
    
    try:
        # Check that heart rate is an integer between 30 and 180 bpm
        hr = int(hr)
        if not (30 <= hr <= 180):
            raise ValueError
    except ValueError:
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return
    
    try:
        # Check that respiratory rate is an integer between 5 and 40 bpm
        rr = int(rr)
        if not (5 <= rr <= 40):
            raise ValueError
    except ValueError:
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return
    
    try:
        # Check that systolic blood pressure is an integer between 70 and 200 mmHg
        sbp = int(sbp)
        if not (70 <= sbp <= 200):
            raise ValueError
    except ValueError:
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return
    
    try:
        # Check that diastolic blood pressure is an integer between 40 and 120 mmHg
        dbp = int(dbp)
        if not (40 <= dbp <= 120):
            raise ValueError
    except ValueError:
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return
    
        # Check that oxygen saturation is an integer between 70 and 100%
    try:
        spo2 = int(spo2)
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return
    except ValueError:
        print("Invalid oxygen saturation. Please enter an integer between 70 and 100.")
        return
    
    # Initialize an empty list for the patient if it doesn't exist
    if patientId not in patients:
        patients[patientId] = []

   # Append the new visit to the patient's visit history
    patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])

    # Append the new visit to the text file
    with open(fileName, 'a') as file:
        file.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")

    # Display success message
    print(f"Visit is saved successfully for Patient #{patientId}")


def findVisitsByDate(patients, year=None, month=None):
    
    if not patients:
        # Handle empty patient dictionary
        return []

    results = []
    for patient_id, visits in patients.items():
        for visit in visits:
            try:
                date_parts = visit[0].split("-")
                visit_year, visit_month, visit_day = map(int, date_parts)
            except (ValueError, IndexError):
                # Handle invalid date format or missing parts
                continue
            
            if year and visit_year != year:
                # Handle year filter
                continue
            if month and visit_month != month:
                # Handle month filter
                continue
            
            # Add visit to results
            results.append((patient_id, visit))

    return results


def findPatientsWhoNeedFollowUp(patients):
    
    followup_patients = []

    for patientId, visits in patients.items():
        for visit in visits:
            if (visit[2] > 100 or visit[2] < 60 
                or visit[4] > 140 or visit[5] > 90 
                or visit[6] < 90):
                followup_patients.append(patientId)
                break
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
   
    # Check if patient exists in dictionary
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")
        return

    # Remove all visits of the patient
    patients[patientId] = []

    # Open the file in write mode
    with open(filename, 'w') as f:
        # Iterate over the dictionary of patient data
        for p_id, visits in patients.items():
            # Write each remaining visit for each patient to the file
            for visit in visits:
                # Write visit data in comma-separated format
                f.write(f"{p_id},{','.join(map(str, visit))}\n")

    print(f"Data for patient {patientId} has been deleted.")


def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = int(input("Enter patient ID (or '0' for all patients): "))
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()