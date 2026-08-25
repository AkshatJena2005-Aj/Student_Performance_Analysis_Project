import pandas as pd


# Load student data from CSV
def load_data():
    return pd.read_csv("student_data.csv")


# Calculate average marks for each student
def calculate_average(df, subjects):
    df["Average"] = df[subjects].mean(axis=1)
    return df


# Categorize students based on their average marks
def performance_category(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 60:
        return "Average"
    else:
        return "Needs Improvement"


# Find subjects where a student scored below 60
def find_weak_subjects(row, subjects):
    weak_subjects = []

    for subject in subjects:
        if row[subject] < 60:
            weak_subjects.append(subject)

    if weak_subjects:
        return ", ".join(weak_subjects) 
    else:
        return "None"


def main():

    # Subjects included in the analysis
    subjects = ["Python", "Pandas", "DSA", "DBMS", "OOP"]

    # Load the dataset
    df = load_data()

    # Display basic information
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    # Calculate student averages
    df = calculate_average(df, subjects)

    # Categorize student performance
    df["Performance"] = df["Average"].apply(performance_category)

    # Identify weak subjects
    df["Weak_Subjects"] = df.apply(
        lambda row: find_weak_subjects(row, subjects),
        axis=1
    )

    # Rank students based on average
    df = df.sort_values(by="Average", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    # Calculate subject-wise averages
    subject_averages = df[subjects].mean()

    # Find highest and lowest performing students
    highest_student = df.loc[df["Average"].idxmax()]
    lowest_student = df.loc[df["Average"].idxmin()]

    # Count students in each performance category
    performance_count = df.groupby("Performance").size()

    # Display final analysis
    print("\n========== STUDENT PERFORMANCE ANALYSIS ==========")

    print("\nStudent Ranking:")
    print(df[[
        "Rank",
        "Name",
        "Average",
        "Performance",
        "Weak_Subjects"
    ]])

    print("\nHighest Performing Student:")
    print(highest_student[["Name", "Average"]])

    print("\nLowest Performing Student:")
    print(lowest_student[["Name", "Average"]])

    print("\nSubject-wise Average:")
    print(subject_averages)

    print("\nBest Performing Subject:")
    print(subject_averages.idxmax())

    print("\nLowest Performing Subject:")
    print(subject_averages.idxmin())

    print("\nPerformance Category Count:")
    print(performance_count)

    # Save the analyzed data
    df.to_csv("student_analysis_result.csv", index=False)

    print("\nAnalysis completed successfully!")
    print("Result saved to student_analysis_result.csv")


# Start the program
if __name__ == "__main__":
    main()