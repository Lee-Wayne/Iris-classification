import openpyxl as xl


def get_avg_data(sheet_name, start_cell, end_cell):
    """get a set of the features from a category, and average it."""
    temp_sum = 0
    data_set = sheet_name[start_cell:end_cell]
    for rows in data_set:
        for c in rows:
            temp_sum += c.value
    data_avg = temp_sum / len(data_set)
    return data_avg


def euclidean_distance_determination_method(sheet_name, start_cell, end_cell):
    """use this method to categorise the testing examples from sheet"""
    outcomes_list = []
    for rows in sheet_name[start_cell:end_cell]:
        x1_sum, x2_sum, x3_sum = 0, 0, 0
        for i in range(len(rows)):
            x1_sum += abs(rows[i].value - setosa_data_list[i])
            x2_sum += abs(rows[i].value - versicolor_data_list[i])
            x3_sum += abs(rows[i].value - virginica_data_list[i])
        min_x = min(x1_sum, x2_sum, x3_sum)
        if min_x == x1_sum:
            category = "Iris-setosa"
        elif min_x == x2_sum:
            category = "Iris-versicolor"
        else:
            category = "Iris-virginica"
        outcomes_list.append(category)
    return outcomes_list


def cal_acc(outcomes_list, test_data_name, start_row, end_row):
    """calculate the accuracy"""
    correct_sum = 0
    test_rows = test_data_name[start_row:end_row]
    for i in range(len(test_rows)):
        if outcomes_list[i] == test_rows[i][0].value:
            correct_sum += 1
    accuracy = correct_sum / len(test_rows)
    return accuracy


# load the file
wb = xl.load_workbook(filename='iris.xlsx')
train_sheet = wb["Training"]
test_sheet = wb["Testing"]
# get iris-setosa's avg data
setosa_data_list = [get_avg_data(train_sheet, 'A1', 'A40'),
                    get_avg_data(train_sheet, 'B1', 'B40'),
                    get_avg_data(train_sheet, 'C1', 'C40'),
                    get_avg_data(train_sheet, 'D1', 'D40')]
# get iris-versicolor's avg data
versicolor_data_list = [get_avg_data(train_sheet, 'A41', 'A80'),
                        get_avg_data(train_sheet, 'B41', 'B80'),
                        get_avg_data(train_sheet, 'C41', 'C80'),
                        get_avg_data(train_sheet, 'D41', 'D80')]
# get iris-virginica's avg data
virginica_data_list = [get_avg_data(train_sheet, 'A81', 'A120'),
                       get_avg_data(train_sheet, 'B81', 'B120'),
                       get_avg_data(train_sheet, 'C81', 'C120'),
                       get_avg_data(train_sheet, 'D81', 'D120')]
# get outcome and calculate the accuracy :D
outcomes = euclidean_distance_determination_method(test_sheet, 'A1', 'D30')
acc = cal_acc(outcomes, test_sheet, 'E1', 'E30')
print(outcomes)
print("Accuracy:", acc)
