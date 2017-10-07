import sys
import dicom
import os.path

# dicom.debug()

if __name__ == "__main__":
    # CD-ROM root
    filepath = "X:\\"
    if os.path.isdir(filepath):  # only gave directory, add standard name
        filepath = os.path.join(filepath, "DICOMDIR")
        dcmdir = dicom.read_dicomdir(filepath)
        base_dir = os.path.dirname(filepath)

        for patrec in dcmdir.patient_records:
            print("Patient: {0.PatientID}:\t"
                  "{0.PatientsName}".format(patrec))

            studies = patrec.children
            for study in studies:
                print("\tStudy {0.StudyID}:\t{0.StudyDate}:\t"
                      "{0.StudyDescription}".format(study))

                all_series = study.children
                for series in all_series:
                    image_count = len(series.children)
                    plural = ('', 's')[image_count > 1]
                    print("\t\tSeries {0.SeriesNumber}\t{0.Modality}\t{0.SeriesDate}"
                          "\t{0.SeriesDescription}\t{1}\timage{2}"
                          .format(series, image_count, plural))
